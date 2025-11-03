
def game_start():
    print("The year is 1718. The Caribbean is a sea of opportunity — for those bold enough to seize it. \nYou’ve just escaped your service aboard a British frigate and find yourself in Nassau, a pirate haven teeming with rogues, sailors, and scoundrels.")
    print("What will you do? \n1.Look for work at the tavern. \n2.Try to join a pirate crew at the docks. \n3. Seek out the local governor for a pardon.")
    decision = input("Type 1, 2, or 3 to select your action.")
    if decision == "1":
        tavern_path()
    elif decision == "2":
        dock_path()
    elif decision == "3":
        forgiveness_path()
    else:
        print("Please type 1, 2, or 3 to choose an option:  ")

def tavern_path():
    print("You enter “The Broken Compass,” where sailors brawl and mugs crash. Behind the bar, a woman with red hair and fierce eyes watches you: Anne Bonny. She eyes you with amusement. \n“You’ve got the look of a man run from the law. The sea’ll either drown you or make you famous. Which is it to be?”")
    print("Decision: \n1.Offer to buy Anne a drink and ask about joining her crew. \n2.Stay quiet and eavesdrop on rumors of buried treasure. \n3. Get involved in a bar fight to prove your courage.")
    decision = input("Type 1, 2, or 3 to select your action.")
    if decision == "1":
        join_anne_crew()
    elif decision == "2":
        eavesdrop_path()
    elif decision == "3":
        bar_fight_path()
    else:
        print("Please type 1, 2, or 3 to choose an option:  ")

def dock_path():
    print("The Revenge, a sleek sloop, rocks gently at the pier. Calico Jack Rackham struts along the gangplank, a feathered hat and gold trim catching the sun.\n“I need daring men. Can you load a cannon without blowing your fingers off?”")
    print("Decision: \n1.Join Rackham \n2.Secretly spy for the Governor \n3.Seek Blackbeard")
    decision = input("Type 1, 2, or 3 to select your action.")
    if decision == "1":
        join_calico_crew()
    elif decision == "2":
        spy_path()
    elif decision == "3":
        plunder_charleston()
    else:
        print("Please type 1, 2, or 3 to choose an option:  ")


def forgiveness_path():
    print("Inside Fort Nassau, Governor Woodes Rogers sits behind a heavy desk.\n“Another deserter, eh? The King offers pardon to all who renounce piracy. Take it, and you might live long enough to grow old.”")
    print("Decision: \n1.Accept the Pardon \n2.Feign Acceptance \n3.Refuse")
    decision = input("Type 1, 2, or 3 to select your action.")
    if decision == "1":
        accept_forgiveness()
    elif decision == "2":
        feign_acceptance()
    elif decision == "3":
        refuse_path()
    else:
        print("Please type 1, 2, or 3 to choose an option:  ")

def join_anne_crew():
    print("You sail under the black flag for the first time. Anne trains you in swordplay, Rackham in charm and deceit. You raid merchant ships and grow infamous. \nAnne: “You learn quick, Reed. The sea likes those who listen — and kills those who don’t.”")
    print("Decision: \n1.Stay loyal to Anne — earn her trust and affection. \n2.Side with Rackham — help him overthrow her. \n3. Plot to take command yourself.")
    decision = input("Type 1, 2, or 3 to select your action.")
    if decision == "1":
       anne_loyalty()
    elif decision == "2":
        jack_path()
    elif decision == "3":
        mutiny_path()
    else:
        print("Please type 1, 2, or 3 to choose an option:  ")

def eavesdrop_path():
    print("You overhear sailors whispering of Captain William Kidd’s lost hoard, buried somewhere in the Bahamas. \nYou steal a map fragment from a drunken smuggler and slip away.\n The fragment reads: “Under twin palms where coral bleeds.”")
    print("Decision: \n1.Search alone — risk everything for glory. \n2.Recruit Anne secretly — share the treasure and the danger. \n3. Sell the map to Bartholomew “Black Bart” Roberts — trade adventure for wealth.")
    decision = input("Type 1, 2, or 3 to select your action.")
    if decision == "1":
       search_alone()
    elif decision == "2":
        search_with_anne()
    elif decision == "3":
        sell_map()
    else:
        print("Please type 1, 2, or 3 to choose an option:  ")

def bar_fight_path():
    print("You knock out two sailors and draw laughter from Anne.\nAnne: “Not bad, for a navy dog. The sea may yet make a wolf of you.”\nShe invites you aboard Revenge II")
    join_anne_crew()


def join_calico_crew():
    print("At the docks, Rackham recruits men while his partner Anne Bonny watches from afar.\nA chained man being dragged by Spanish soldiers catches your eye — it’s Charles Vane, the infamous captain who defied Woodes Rogers.\nVane: “Cut me loose, boy, and I’ll make you rich beyond your dreams!”")
    print("Decision:\n1.Join Rackham’s crew — plunder, fame, and debauchery.\n2.Rescue Charles Vane — risk everything for an alliance.\n3.Spy for the governor — betray the pirates for a pardon.")
    decision = input("Type 1, 2, or 3 to select your action.")
    if decision == "1":
       calico_crew()
    elif decision == "2":
        rescue_vane()
    elif decision == "3":
        spy_path()
    else:
        print("Please type 1, 2, or 3 to choose an option:  ")

def calico_crew():
    print("Life aboard Revenge is wild: raids, rum, and rebellion.\nRackham is bold but reckless. Anne’s jealousy simmers.\nDuring a raid on a Spanish fort, Vane reappears — chained in the brig of a captured ship.")
    print("Decision:\n1.Free Vane secretly — gain his respect.\n2.Ignore him — stay loyal to Rackham.\n3.Release him openly — spark a mutiny.")
    decision = input("Type 1, 2, or 3 to select your action.")
    if decision == "1":
       vane_alliance()
    elif decision == "2":
        rackhams_approval()
    elif decision == "3":
        mutiny()
    else:
        print("Please type 1, 2, or 3 to choose an option:  ")

def rescue_vane():
    print("You ambush the Spaniards and free Vane. He grins.\nVane: “The sea’s got room for bold men, not cowards hiding behind flags.”\nHe invites you to join his ship, The Ranger. \nTogether, you raid the Jamaican coast — but Vane’s cruelty grows.")
    print("Decision:\n1.Challenge his command — duel for control.\n2.Endure his madness — wait for a chance.\n3.Abandon him — flee in the night.")
    decision = input("Type 1, 2, or 3 to select your action.")
    if decision == "1":
       dual_for_command()
    elif decision == "2":
        captured_by_roberts()
    elif decision == "3":
        join_roberts()
    else:
        print("Please type 1, 2, or 3 to choose an option:  ")


def spy_path():
    print("Each night, you pass secret notes to the governor’s men.\nYour information leads to the capture of several pirate ships — and eventually, Rackham himself.\nRogers: “Well done, Reed. Your treachery buys your freedom.”\nBut your conscience gnaws at you.\nYou’re rich, but despised — a traitor among pirates and men.")
    hangmans_noose()

def accept_forgiveness():
    print("You sign the pardon.\nYears pass as you serve aboard British privateers against Spain.\nThe pirate republic of Nassau falls in 1718 — Blackbeard is killed that same year off Ocracoke by Lieutenant Maynard.\nYou watch from a distance as the age of piracy dies.")
    gentleman_privateer()

def feign_acceptance():
    print("You accept the pardon, then sell your knowledge to the pirates.\nCharles Vane welcomes you as a double agent — until your letters to Rogers are discovered.\nYou’re dragged to the gallows, shouting,\n“I fought for freedom, not a king!”")
    rope_at_dawn()

def refuse_path():
    print("You escape Nassau under fire and sail north to Ocracoke Inlet, where Blackbeard rules.\nHis ship, Queen Anne’s Revenge, towers over the water like a fortress of smoke. \nBlackbeard: “Serve me, lad. The sea bows to no crown.”")
    print("1.Join him — live in his shadow, raiding the Carolinas.\n2.Challenge him — fight the legend himself.\n3.Betray him — report him to the British.")
    decision = input("Type 1, 2, or 3 to select your action.")
    if decision == "1":
       plunder_charleston()
    elif decision == "2":
        kill_blackbeard()
    elif decision == "3":
        rewarded_richly()
    else:
        print("Please type 1, 2, or 3 to choose an option:  ")


def anne_loyalty():
    print("You stay loyal to Anne even as the crew whispers about mutiny.\nRackham mocks her leadership, calling her “the captain’s whore.” You strike him across the face before the words finish.\nAnne: “You didn’t have to do that.”\nYou: “A captain deserves respect.”\nAnne: “Then I’ll make sure you get yours.”\nTogether, you lead Revenge II on daring raids across the Windward Passage, plundering sugar barges and merchant ships. The Royal Navy posts a bounty on your head.\nBy 1720, Woodes Rogers’s forces tighten around Nassau. Rackham is captured; Anne escapes disguised as a man. You and she flee to a hidden cay.\nAt dawn, she looks at the horizon.\nAnne: “No king, no ropes, no regrets. That’s freedom, isn’t it?”\nYou: “Aye, love. For as long as the sea keeps our names.”")
    lovers_fortune()

def jack_path():
    print("You side with Rackham when he challenges Anne’s command.\nIn the dead of night, the crew gathers — pistols, cutlasses, torches.\nRackham: “No woman leads me! Reed, stand with me and we’ll sail under my flag alone.”\nAnne fights like a storm, cutting down two men before she’s overpowered. Rackham spares her life — at your insistence — but sends her ashore at Tortuga.\nRackham names you quartermaster. Fame follows. But Rackham’s vanity and drink drive the ship into chaos.\nIn October 1720, the British sloop Snow-Tyger catches you off Negril. The crew, too drunk to fight, is slaughtered.\nAnne (before capture): “If you’d fought like a man, Jack, you’d not hang like a dog!”")
    rope_at_dawn()


def mutiny_path():
    print("Anne and Rackham’s constant quarrels weaken morale.\nYou quietly promise gold and discipline to the weary crew. One stormy night, you seize command.\nAnne: “You’d stab us in our sleep for a few extra shares?”\nYou: “No. For order.”\nYour new reign is short-lived. Rackham’s loyalists fire the powder magazine in revenge.\nYou order the cannons turned on both rebels and pursuers — a blaze that lights the night sea.")
    blood_and_thunder()


def search_alone():
    print("You sail by night to an uncharted cay. The palms bend like watchful sentries.\nThe map fragment leads you inland to a coral pit. You dig until your hands bleed.\nYour shovel strikes wood — a chest filled with Spanish coins and rubies.\nA musket cracks. Spanish marines appear from the trees.\nYou: “This gold’s mine!”\nThey fire. You fall, the chest open beside you.\nAs the tide rolls in, waves cover your body and scatter the treasure.")
    lonely_treasure()

def search_with_anne():
    print("You show Anne the map. Her eyes glitter.\nAnne: “Half for me, half for you — unless one of us shoots first.”\nTogether, you sail to the cay. You find the chest beneath twin palms — Kidd’s treasure, untouched.\nAnne laughs as you lift the lid.\nAnne: “All the gold in the world won’t buy a quiet heart.”\nYou: “Then we’ll live loud, till the sea takes us.”\nYou hide the treasure and vanish into the mists of the Caribbean.")
    lovers_fortune()

def sell_map():
    print("You bring the fragment to Black Bart Roberts — the most feared pirate of 1720.\nHe examines it with a smile.\nRoberts: “I’ll give you ten thousand in coin, and a safe berth. Take the deal or lose your head.”\nYou take it. Gold flows like rum for months.\nBut wealth draws envy. One night in Port Royal, a serving girl pours you wine. It tastes bitter.\nYou: “What—?”\nPoisoner: “Black Bart sends his regards.”")
    golds_curse()

def vane_alliance():
    print("You sneak below decks, cutting Vane’s bonds.\nVane: “A bold move, lad. You’ll not regret it.”\nHe vanishes into the night. Rackham never learns the truth.\nMonths later, during a naval ambush near Jamaica, The Ranger appears — Vane’s ship. He saves you, cannons roaring.\nVane: “Didn’t I say you’d not regret it?”\nYou and Vane unite your crews, raiding Kingston’s harbor before vanishing east.")
    pirate_king()

def rackhams_approval():
    print("You look away as Vane is hauled off in chains. Rackham claps your shoulder.\nRackham: “Good sense, lad. Mercy gets you killed.”\nThe raids continue — until the Royal Navy corners you. The crew is too drunk to fight.\nRackham is captured; Anne curses him. You’re hanged beside them.")
    rope_at_dawn()

def mutiny():
    print("You draw your sword, shouting,\nYou: “This man’s a pirate, not a prisoner! I’ll see no brother hang!”\nThe deck erupts in chaos. Rackham flees below deck, and Anne fires her pistol into the air.\nVane joins you, laughing.\nVane: “That’s the spirit! Let the sea decide our fates.”\nTogether, you capture the ship but are pursued by two British sloops.\nVane refuses to surrender; you steer into them, guns blazing.")
    blood_and_thunder()

def dual_for_command():
    print("Vane’s cruelty grows unbearable — marooned prisoners, burned villages.When he orders your crew to torch a captured sloop full of civilians, you step forward.You: “No more. You’ve become the tyrant you fled.”Vane: “Then face me!”\nYou duel on the quarterdeck amid rain and thunder.\nYour blade pierces his heart. The crew hails you captain.\nFor two years you reign, ruthless but respected — until 1722, when a British frigate ambushes you off Barbados.")
    pirate_king()

def captured_by_roberts():
    print("You stay silent as Vane grows paranoid.\nEventually, the crew mutinies and hands him over to Governor Rogers.\nHe hangs in 1721. You watch from the crowd, hooded.\nVane: “Hang me if you must. I’d rather swing than kneel.”\nYou slip away, a ghost of a dying age.")
    ghost_of_carribean()

def join_roberts():
    print("You desert Vane’s ship one night and find refuge aboard the Royal Fortune under Bartholomew Roberts.\nRoberts is disciplined, elegant, and cold.\nRoberts: “A pirate must have order, or he’s no better than a thief.”\nUnder his black flag, you raid the Gold Coast and Spanish Main. When Roberts is killed in 1722, you take the helm briefly before the Navy overwhelms you.")
    blood_and_thunder()

def plunder_charleston():
    print("At Ocracoke, Edward Teach towers over you, smoke curling from fuses in his beard.\nBlackbeard: “Serve me, lad, and we’ll make the seas tremble.”\nYou plunder Charleston, blockading the harbor.\nIn November 1718, Maynard’s sloop ambushes you. You fight beside Blackbeard until he’s struck down — five bullets, twenty wounds.\nYou flee with the survivors, taking command of Queen Anne’s Revenge.")
    blood_and_thunder()

def kill_blackbeard():
    print("You confront him before the crew.\nYou: “You’ve had your day, Teach. Now it’s mine.”\nBlackbeard: “Then come take it!”\nYou fight for an hour — swords ringing, pistols flashing.\nYou run him through. The men cheer, and you take the black flag for yourself.\nFor a year, you rule his fleet, feared across the Carolinas, until the Navy returns with vengeance.")
    pirate_king()

def rewarded_richly():
    print("You slip a note to Rogers’s agent in New Providence: “Teach hides at Ocracoke.\nAt dawn, Maynard’s ships attack.\nBlackbeard dies fighting, and his head is hung from a bowsprit.\nRogers rewards you with gold and a privateer’s license.\nBut whispers follow you — “the man who sold the Devil.”")
    hangmans_noose()

def pirate_king():
    print("You unite Anne Bonny, Charles Vane, and Black Bart Roberts under your flag.\nTogether, you fight the British in a final battle off Barbados.\nYour ship sinks in flames — but songs of Captain Thomas Reed, the Pirate King echo for centuries.")

def lovers_fortune():
    print("You and Anne Bonny discover Captain Kidd’s treasure and vanish.\nYears later, islanders whisper of two lovers who ruled a hidden cove of gold.")

def lonely_treasure():
    print("You die defending your buried gold from marines.\nWaves bury you beside your chest — the sea your only witness.")

def golds_curse():
    print("You sell the map and live like a lord in Jamaica — until a rival poisons your rum.\n“Gold bought your comfort,” your killer says, “and your coffin.”")

def gentleman_privateer():
    print("You fight for the Crown, capturing your old comrades.\nWhen Rogers dies in 1732, you stand at his grave, unsure if you mourn him or yourself.")

def rope_at_dawn():
    print("You’re caught and hanged in Nassau Square, alongside Vane and Rackham.\n“Pirates!” cries the crowd. “Murderers!”\nYou smile. “Free men,” you whisper.")

def ghost_of_carribean():
    print("Your ship, The Liberty’s End, vanishes in a storm.\nYears later, sailors swear they see its tattered sails on moonless nights, chasing Spanish gold.")

def blood_and_thunder():
    print("Cannons blaze as you ram a British frigate.\nYour crew cheers as the ship explodes — your name forever etched in blood and smoke.\n“To freedom!” are your last words.")

def hangmans_noose():
    print("The sky over Nassau is pale and unforgiving.\nA gallows has been raised on the hill above the harbor — a cruel silhouette against the morning sun. The crowd below is thick with merchants, sailors, and soldiers, all eager for a glimpse of justice served.\nYou stand upon the platform, wrists bound, the rope rough against your neck. The air smells of tar and salt. The lever drops. The rope tightens. The world goes white.\nFor a heartbeat, you feel the wind rush past your face, and the memory of open sails fills your mind \nAnne’s laughter, Blackbeard’s roar, Rackham’s grin, the taste of rum, the smell of gunpowder.\nThen nothing but silence.\nBelow, a sailor removes his hat.\n“A pirate,” he mutters, “and a fool.”\nThe hangman wipes his hands. The crowd disperses.\nBy nightfall, only the gulls remain — and the sea, carrying your story away with the tide.")



game_start()