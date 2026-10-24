
import threading
import time
import queue

class Message:
    def __init__(self, msg_type, estampille, emetteur):
        self.type = msg_type
        self.estampille = estampille
        self.emetteur = emetteur
        
    def __repr__(self):
        return f"({self.type}, {self.estampille}, S{self.emetteur})"

class Site(threading.Thread):
    def __init__(self, id_site, nb_sites):
        super().__init__(name=f"S{id_site}")
        self.id = id_site
        self.nb_sites = nb_sites
        self.date = 0
        # Initialisation de la file : chaque site est supposé être en état REL
        self.file = {i: Message('REL', 0, i) for i in range(nb_sites)}
        self.boite_lettres = queue.Queue()
        self.sites_voisins = {}
        self.en_cours = True
        
        # Verrou pour protéger l'accès concurrent aux variables locales (date, file)
        self.lock = threading.Lock()
        # Condition pour réveiller le thread quand il attend la section critique
        self.condition = threading.Condition(self.lock)

    def connect(self, reseau_sites):
        self.sites_voisins = reseau_sites

    def diffuser(self, msg):
        for id_voisin, voisin in self.sites_voisins.items():
            if id_voisin != self.id:
                voisin.boite_lettres.put(msg)

    def envoyer(self, msg, dest_id):
        self.sites_voisins[dest_id].boite_lettres.put(msg)

    def entree_section(self):
        with self.condition:
            # diffuser (demande, date, i)
            msg = Message('REQ', self.date, self.id)
            self.diffuser(msg)
            
            # file[i] := (demande, date, i)
            self.file[self.id] = msg
            
            # date := date + 1
            self.date += 1
            
            print(f"[S{self.id}] ⏳ Demande SC (Estampille: {msg.estampille})")

            # tant que (il existe j / (file[j].estampille, j) < (file[i].estampille, i)) faire rien
            while not self._peut_entrer():
                self.condition.wait()
            print(f"[S{self.id}] 🟢 ENTRE EN SECTION CRITIQUE")

    def _peut_entrer(self):
        mon_msg = self.file[self.id]
        mon_couple = (mon_msg.estampille, self.id)
        
        for j in range(self.nb_sites):
            if j == self.id:
                continue
            autre_msg = self.file[j]
            autre_couple = (autre_msg.estampille, j)
            
            # L'exclusion mutuelle : un autre site a un message plus prioritaire
            if autre_couple < mon_couple:
                return False
        return True

    def sortie_section(self):
        with self.condition:
            print(f"[S{self.id}] 🔴 SORT DE LA SECTION CRITIQUE")
            # diffuser (REL, date, i)
            msg = Message('REL', self.date, self.id)
            self.diffuser(msg)
            
            # file[i] := (REL, date, i)
            self.file[self.id] = msg
            
            # date := date + 1
            self.date += 1

    def traiter_message(self, arrivée):
        with self.condition:
            # date = max(date, arrivée.estampille)
            self.date = max(self.date, arrivée.estampille)
            # date := date + 1
            self.date += 1
            
            # case arrivée.type sous
            if arrivée.type == 'REQ':
                # file[arrivée.emetteur] := arrivée
                self.file[arrivée.emetteur] = arrivée
                
                # envoyer ((ACK, date, i), arrivée.emetteur)
                ack = Message('ACK', self.date, self.id)
                self.envoyer(ack, arrivée.emetteur)
                
            elif arrivée.type == 'REL':
                # file[arrivée.emetteur] := arrivée
                self.file[arrivée.emetteur] = arrivée
                
            elif arrivée.type == 'ACK':
                # si file[arrivée.emetteur].type != REQ alors file[arrivée.emetteur] := arrivée
                if self.file[arrivée.emetteur].type != 'REQ':
                    self.file[arrivée.emetteur] = arrivée
                    
            # Un changement dans le tableau peut débloquer l'entrée en section critique
            self.condition.notify_all()

    def run(self):
        while self.en_cours:
            try:
                msg = self.boite_lettres.get(timeout=0.2)
                self.traiter_message(msg)
            except queue.Empty:
                pass

# --- Script de simulation ---
def main():
    print("=== Algorithme de Lamport : Test d'Exclusion Mutuelle ===")
    nb_sites = 3
    sites = {i: Site(i, nb_sites) for i in range(nb_sites)}
    
    # Interconnexion réseau
    for i in range(nb_sites):
        sites[i].connect(sites)
        sites[i].start()
        
    time.sleep(1)
    
    # S0 et S1 demandent la section critique simultanément
    t0 = threading.Thread(target=sites[0].entree_section)
    t1 = threading.Thread(target=sites[1].entree_section)
    
    t0.start()
    t1.start()
    
    # Laisser le temps à S0 (prioritaire si estampilles égales) d'entrer en SC
    time.sleep(2)
    sites[0].sortie_section()
    
    # S1 devrait entrer à son tour
    time.sleep(2)
    sites[1].sortie_section()
    
    time.sleep(1)
    # Arrêt propre
    for s in sites.values():
        s.en_cours = False
        s.join()
        
    print("=== Fin de la simulation ===")

if __name__ == '__main__':
    main()
