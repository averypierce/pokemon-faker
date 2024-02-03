from bs4 import BeautifulSoup

html = """
                                        <div class="mw-category-group">
                                            <h3>A</h3>
                                            <ul>
                                                <li><a href="/wiki/A-list_Actor_(Trainer_class)"
                                                        title="A-list Actor (Trainer class)">A-list Actor (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Ace_Duo_(Trainer_class)"
                                                        title="Ace Duo (Trainer class)">Ace Duo (Trainer class)</a></li>
                                                <li><a href="/wiki/Ace_Trainer_(Trainer_class)"
                                                        title="Ace Trainer (Trainer class)">Ace Trainer (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Actor_(Trainer_class)"
                                                        title="Actor (Trainer class)">Actor (Trainer class)</a></li>
                                                <li><a href="/wiki/Actress_(Trainer_class)"
                                                        title="Actress (Trainer class)">Actress (Trainer class)</a></li>
                                                <li><a href="/wiki/Aeos_Trainer_(Trainer_class)"
                                                        title="Aeos Trainer (Trainer class)">Aeos Trainer (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Aether_Foundation_(Trainer_class)"
                                                        title="Aether Foundation (Trainer class)">Aether Foundation
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Aether_Foundation_Employee_(Trainer_class)"
                                                        title="Aether Foundation Employee (Trainer class)">Aether
                                                        Foundation Employee (Trainer class)</a></li>
                                                <li><a href="/wiki/Aqua_Admin_(Trainer_class)"
                                                        title="Aqua Admin (Trainer class)">Aqua Admin (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Area_Leader_(Trainer_class)"
                                                        title="Area Leader (Trainer class)">Area Leader (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Aroma_Lady_(Trainer_class)"
                                                        title="Aroma Lady (Trainer class)">Aroma Lady (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Artist_(Trainer_class)"
                                                        title="Artist (Trainer class)">Artist (Trainer class)</a></li>
                                                <li><a href="/wiki/Artist_Family_(Trainer_class)"
                                                        title="Artist Family (Trainer class)">Artist Family (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Assistant_(Trainer_class)"
                                                        title="Assistant (Trainer class)">Assistant (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Athlete_(Trainer_class)"
                                                        title="Athlete (Trainer class)">Athlete (Trainer class)</a></li>
                                                <li><a href="/wiki/Athletic_Siblings_(Trainer_class)"
                                                        title="Athletic Siblings (Trainer class)">Athletic Siblings
                                                        (Trainer class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>B</h3>
                                            <ul>
                                                <li><a href="/wiki/Backers_(Trainer_class)"
                                                        title="Backers (Trainer class)">Backers (Trainer class)</a></li>
                                                <li><a href="/wiki/Backpacker_(Trainer_class)"
                                                        title="Backpacker (Trainer class)">Backpacker (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Baker_(Trainer_class)"
                                                        title="Baker (Trainer class)">Baker (Trainer class)</a></li>
                                                <li><a href="/wiki/Bandana_Guy_(Trainer_class)"
                                                        title="Bandana Guy (Trainer class)">Bandana Guy (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Bandit_(Trainer_class)"
                                                        title="Bandit (Trainer class)">Bandit (Trainer class)</a></li>
                                                <li><a href="/wiki/Baron_(Trainer_class)"
                                                        title="Baron (Trainer class)">Baron (Trainer class)</a></li>
                                                <li><a href="/wiki/Baroness_(Trainer_class)"
                                                        title="Baroness (Trainer class)">Baroness (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Battle_Chatelaine_(Trainer_class)"
                                                        title="Battle Chatelaine (Trainer class)">Battle Chatelaine
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Battle_Girl_(Trainer_class)"
                                                        title="Battle Girl (Trainer class)">Battle Girl (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Battle_Legend_(Trainer_class)"
                                                        title="Battle Legend (Trainer class)">Battle Legend (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/BB_League_Elite_Four_(Trainer_class)"
                                                        title="BB League Elite Four (Trainer class)">BB League Elite
                                                        Four (Trainer class)</a></li>
                                                <li><a href="/wiki/Beauty_(Trainer_class)"
                                                        title="Beauty (Trainer class)">Beauty (Trainer class)</a></li>
                                                <li><a href="/wiki/Beginning_Trainer_(Trainer_class)"
                                                        title="Beginning Trainer (Trainer class)">Beginning Trainer
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Bellhop_(Trainer_class)"
                                                        title="Bellhop (Trainer class)">Bellhop (Trainer class)</a></li>
                                                <li><a href="/wiki/Big_Star_(Trainer_class)"
                                                        title="Big Star (Trainer class)">Big Star (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Biker_(Trainer_class)"
                                                        title="Biker (Trainer class)">Biker (Trainer class)</a></li>
                                                <li><a href="/wiki/Bird_Keeper_(Trainer_class)"
                                                        title="Bird Keeper (Trainer class)">Bird Keeper (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Black_Belt_(Trainer_class)"
                                                        title="Black Belt (Trainer class)">Black Belt (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Boarder_(Trainer_class)"
                                                        title="Boarder (Trainer class)">Boarder (Trainer class)</a></li>
                                                <li><a href="/wiki/Bodybuilder_(Trainer_class)"
                                                        title="Bodybuilder (Trainer class)">Bodybuilder (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Boss_Trainer_(Trainer_class)"
                                                        title="Boss Trainer (Trainer class)">Boss Trainer (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Brains_%26_Brawn_(Trainer_class)"
                                                        title="Brains &amp; Brawn (Trainer class)">Brains &amp; Brawn
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Bug_Catcher_(Trainer_class)"
                                                        title="Bug Catcher (Trainer class)">Bug Catcher (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Bug_Maniac_(Trainer_class)"
                                                        title="Bug Maniac (Trainer class)">Bug Maniac (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Bug-Catching_Man_(Trainer_class)"
                                                        title="Bug-Catching Man (Trainer class)">Bug-Catching Man
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Burglar_(Trainer_class)"
                                                        title="Burglar (Trainer class)">Burglar (Trainer class)</a></li>
                                                <li><a href="/wiki/Butler_(Trainer_class)"
                                                        title="Butler (Trainer class)">Butler (Trainer class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>C</h3>
                                            <ul>
                                                <li><a href="/wiki/Cabbie_(Trainer_class)"
                                                        title="Cabbie (Trainer class)">Cabbie (Trainer class)</a></li>
                                                <li><a href="/wiki/Caf%C3%A9_Master_(Trainer_class)"
                                                        title="Café Master (Trainer class)">Café Master (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Cameraman_(Trainer_class)"
                                                        title="Cameraman (Trainer class)">Cameraman (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Camper_(Trainer_class)"
                                                        title="Camper (Trainer class)">Camper (Trainer class)</a></li>
                                                <li><a href="/wiki/Capoeira_Couple_(Trainer_class)"
                                                        title="Capoeira Couple (Trainer class)">Capoeira Couple (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Casual_Dude_(Trainer_class)"
                                                        title="Casual Dude (Trainer class)">Casual Dude (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Casual_Guy_(Trainer_class)"
                                                        title="Casual Guy (Trainer class)">Casual Guy (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Celebrity_(Trainer_class)"
                                                        title="Celebrity (Trainer class)">Celebrity (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Challenger_(Trainer_class)"
                                                        title="Challenger (Trainer class)">Challenger (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Channeler_(Trainer_class)"
                                                        title="Channeler (Trainer class)">Channeler (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Chaser_(Trainer_class)"
                                                        title="Chaser (Trainer class)">Chaser (Trainer class)</a></li>
                                                <li><a href="/wiki/Chef_(Trainer_class)"
                                                        title="Chef (Trainer class)">Chef (Trainer class)</a></li>
                                                <li><a href="/wiki/Chic_Actress_(Trainer_class)"
                                                        title="Chic Actress (Trainer class)">Chic Actress (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Child_Star_(Trainer_class)"
                                                        title="Child Star (Trainer class)">Child Star (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Cipher_Admin_(Trainer_class)"
                                                        title="Cipher Admin (Trainer class)">Cipher Admin (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Cipher_Peon_(Trainer_class)"
                                                        title="Cipher Peon (Trainer class)">Cipher Peon (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Clan_Leader_(Trainer_class)"
                                                        title="Clan Leader (Trainer class)">Clan Leader (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Close_Siblings_(Trainer_class)"
                                                        title="Close Siblings (Trainer class)">Close Siblings (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Clown_(Trainer_class)"
                                                        title="Clown (Trainer class)">Clown (Trainer class)</a></li>
                                                <li><a href="/wiki/Coach_Trainer_(Trainer_class)"
                                                        title="Coach Trainer (Trainer class)">Coach Trainer (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Colleagues_(Trainer_class)"
                                                        title="Colleagues (Trainer class)">Colleagues (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Collector_(Trainer_class)"
                                                        title="Collector (Trainer class)">Collector (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Colosseum_Leader_(Trainer_class)"
                                                        title="Colosseum Leader (Trainer class)">Colosseum Leader
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Colosseum_Master_(Trainer_class)"
                                                        title="Colosseum Master (Trainer class)">Colosseum Master
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Comedian_(Trainer_class)"
                                                        title="Comedian (Trainer class)">Comedian (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Commander_(Trainer_class)"
                                                        title="Commander (Trainer class)">Commander (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Cook_(Trainer_class)"
                                                        title="Cook (Trainer class)">Cook (Trainer class)</a></li>
                                                <li><a href="/wiki/Cool_Beauty_(Trainer_class)"
                                                        title="Cool Beauty (Trainer class)">Cool Beauty (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Cool_Couple_(Trainer_class)"
                                                        title="Cool Couple (Trainer class)">Cool Couple (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Countess_(Trainer_class)"
                                                        title="Countess (Trainer class)">Countess (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Courier_(Trainer_class)"
                                                        title="Courier (Trainer class)">Courier (Trainer class)</a></li>
                                                <li><a href="/wiki/Cowgirl_(Trainer_class)"
                                                        title="Cowgirl (Trainer class)">Cowgirl (Trainer class)</a></li>
                                                <li><a href="/wiki/Crush_Girl_(Trainer_class)"
                                                        title="Crush Girl (Trainer class)">Crush Girl (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Crush_Kin_(Trainer_class)"
                                                        title="Crush Kin (Trainer class)">Crush Kin (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Curmudgeon_(Trainer_class)"
                                                        title="Curmudgeon (Trainer class)">Curmudgeon (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Cute_Maniac_(Trainer_class)"
                                                        title="Cute Maniac (Trainer class)">Cute Maniac (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Cute_Trainer_(Trainer_class)"
                                                        title="Cute Trainer (Trainer class)">Cute Trainer (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Cyclist_(Trainer_class)"
                                                        title="Cyclist (Trainer class)">Cyclist (Trainer class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>D</h3>
                                            <ul>
                                                <li><a href="/wiki/Dancer_(Trainer_class)"
                                                        title="Dancer (Trainer class)">Dancer (Trainer class)</a></li>
                                                <li><a href="/wiki/Dancing_Family_(Trainer_class)"
                                                        title="Dancing Family (Trainer class)">Dancing Family (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Daring_Couple_(Trainer_class)"
                                                        title="Daring Couple (Trainer class)">Daring Couple (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Delinquent_(Trainer_class)"
                                                        title="Delinquent (Trainer class)">Delinquent (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Doctor_(Trainer_class)"
                                                        title="Doctor (Trainer class)">Doctor (Trainer class)</a></li>
                                                <li><a href="/wiki/Double_Team_(Trainer_class)"
                                                        title="Double Team (Trainer class)">Double Team (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Dragon_Tamer_(Trainer_class)"
                                                        title="Dragon Tamer (Trainer class)">Dragon Tamer (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Driver_(Trainer_class)"
                                                        title="Driver (Trainer class)">Driver (Trainer class)</a></li>
                                                <li><a href="/wiki/Duchess_(Trainer_class)"
                                                        title="Duchess (Trainer class)">Duchess (Trainer class)</a></li>
                                                <li><a href="/wiki/Duke_(Trainer_class)"
                                                        title="Duke (Trainer class)">Duke (Trainer class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>E</h3>
                                            <ul>
                                                <li><a href="/wiki/Earl_(Trainer_class)"
                                                        title="Earl (Trainer class)">Earl (Trainer class)</a></li>
                                                <li><a href="/wiki/Eevee_users" title="Eevee users">Eevee users</a></li>
                                                <li><a href="/wiki/Electrifying_Guy_(Trainer_class)"
                                                        title="Electrifying Guy (Trainer class)">Electrifying Guy
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Elite_Four" title="Elite Four">Elite Four</a></li>
                                                <li><a href="/wiki/Engineer_(Trainer_class)"
                                                        title="Engineer (Trainer class)">Engineer (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Executive_(Trainer_class)"
                                                        title="Executive (Trainer class)">Executive (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Expert_(Trainer_class)"
                                                        title="Expert (Trainer class)">Expert (Trainer class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>F</h3>
                                            <ul>
                                                <li><a href="/wiki/Factory_Head_(Trainer_class)"
                                                        title="Factory Head (Trainer class)">Factory Head (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Fairy_Tale_Girl_(Trainer_class)"
                                                        title="Fairy Tale Girl (Trainer class)">Fairy Tale Girl (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Fare_Prince_(Trainer_class)"
                                                        title="Fare Prince (Trainer class)">Fare Prince (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Festival_Boy_(Trainer_class)"
                                                        title="Festival Boy (Trainer class)">Festival Boy (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Festival_Girl_(Trainer_class)"
                                                        title="Festival Girl (Trainer class)">Festival Girl (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Fine_Actor_(Trainer_class)"
                                                        title="Fine Actor (Trainer class)">Fine Actor (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Firebreather_(Trainer_class)"
                                                        title="Firebreather (Trainer class)">Firebreather (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Firefighter_(Trainer_class)"
                                                        title="Firefighter (Trainer class)">Firefighter (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Fisher_(Trainer_class)"
                                                        title="Fisher (Trainer class)">Fisher (Trainer class)</a></li>
                                                <li><a href="/wiki/Free_Diver_(Trainer_class)"
                                                        title="Free Diver (Trainer class)">Free Diver (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Freshwoman_(Trainer_class)"
                                                        title="Freshwoman (Trainer class)">Freshwoman (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Fun_Old_Man_(Trainer_class)"
                                                        title="Fun Old Man (Trainer class)">Fun Old Man (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Furisode_Girl_(Trainer_class)"
                                                        title="Furisode Girl (Trainer class)">Furisode Girl (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Future_Girl_(Trainer_class)"
                                                        title="Future Girl (Trainer class)">Future Girl (Trainer
                                                        class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>G</h3>
                                            <ul>
                                                <li><a href="/wiki/GAME_FREAK%27s_(Trainer_class)"
                                                        title="GAME FREAK&#039;s (Trainer class)">GAME FREAK&#039;s
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Gardener_(Trainer_class)"
                                                        title="Gardener (Trainer class)">Gardener (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Gar%C3%A7on_(Trainer_class)"
                                                        title="Garçon (Trainer class)">Garçon (Trainer class)</a></li>
                                                <li><a href="/wiki/Gentleman_(Trainer_class)"
                                                        title="Gentleman (Trainer class)">Gentleman (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Girl_In_Love_(Trainer_class)"
                                                        title="Girl In Love (Trainer class)">Girl In Love (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Girlfriend_(Trainer_class)"
                                                        title="Girlfriend (Trainer class)">Girlfriend (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Glasses_Man_(Trainer_class)"
                                                        title="Glasses Man (Trainer class)">Glasses Man (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Glitch_Trainer" title="Glitch Trainer">Glitch
                                                        Trainer</a></li>
                                                <li><a href="/wiki/Golf_Buddies_(Trainer_class)"
                                                        title="Golf Buddies (Trainer class)">Golf Buddies (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Golfer_(Trainer_class)"
                                                        title="Golfer (Trainer class)">Golfer (Trainer class)</a></li>
                                                <li><a href="/wiki/Grand_Duchess_(Trainer_class)"
                                                        title="Grand Duchess (Trainer class)">Grand Duchess (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Grand_Duke_(Trainer_class)"
                                                        title="Grand Duke (Trainer class)">Grand Duke (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Guitarist_(Trainer_class)"
                                                        title="Guitarist (Trainer class)">Guitarist (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Guy_(Trainer_class)" title="Guy (Trainer class)">Guy
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Gym_Challenger_(Trainer_class)"
                                                        title="Gym Challenger (Trainer class)">Gym Challenger (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Gym_Leader" title="Gym Leader">Gym Leader</a></li>
                                                <li><a href="/wiki/Gym_Trainer_(Trainer_class)"
                                                        title="Gym Trainer (Trainer class)">Gym Trainer (Trainer
                                                        class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>H</h3>
                                            <ul>
                                                <li><a href="/wiki/Hardheaded_Girl_(Trainer_class)"
                                                        title="Hardheaded Girl (Trainer class)">Hardheaded Girl (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Harlequin_(Trainer_class)"
                                                        title="Harlequin (Trainer class)">Harlequin (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Haunted_Man_(Trainer_class)"
                                                        title="Haunted Man (Trainer class)">Haunted Man (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Hex_Maniac_(Trainer_class)"
                                                        title="Hex Maniac (Trainer class)">Hex Maniac (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/High-Tech_Maniac_(Trainer_class)"
                                                        title="High-Tech Maniac (Trainer class)">High-Tech Maniac
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Hiker_(Trainer_class)"
                                                        title="Hiker (Trainer class)">Hiker (Trainer class)</a></li>
                                                <li><a href="/wiki/Hiking_Club_Member_(Trainer_class)"
                                                        title="Hiking Club Member (Trainer class)">Hiking Club Member
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Hiking_Girl_(Trainer_class)"
                                                        title="Hiking Girl (Trainer class)">Hiking Girl (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Honeymooners_(Trainer_class)"
                                                        title="Honeymooners (Trainer class)">Honeymooners (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Hooligans_(Trainer_class)"
                                                        title="Hooligans (Trainer class)">Hooligans (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Hoopster_(Trainer_class)"
                                                        title="Hoopster (Trainer class)">Hoopster (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Hunter_(Trainer_class)"
                                                        title="Hunter (Trainer class)">Hunter (Trainer class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>I</h3>
                                            <ul>
                                                <li><a href="/wiki/Icy_Guy_(Trainer_class)"
                                                        title="Icy Guy (Trainer class)">Icy Guy (Trainer class)</a></li>
                                                <li><a href="/wiki/Idol_(Trainer_class)"
                                                        title="Idol (Trainer class)">Idol (Trainer class)</a></li>
                                                <li><a href="/wiki/Infielder_(Trainer_class)"
                                                        title="Infielder (Trainer class)">Infielder (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Instructor_(Trainer_class)"
                                                        title="Instructor (Trainer class)">Instructor (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Interviewers_(Trainer_class)"
                                                        title="Interviewers (Trainer class)">Interviewers (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Island_kahuna" title="Island kahuna">Island
                                                        kahuna</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>J</h3>
                                            <ul>
                                                <li><a href="/wiki/Janitor_(Trainer_class)"
                                                        title="Janitor (Trainer class)">Janitor (Trainer class)</a></li>
                                                <li><a href="/wiki/Joe%27s_Groupie_(Trainer_class)"
                                                        title="Joe&#039;s Groupie (Trainer class)">Joe&#039;s Groupie
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Jogger_(Trainer_class)"
                                                        title="Jogger (Trainer class)">Jogger (Trainer class)</a></li>
                                                <li><a href="/wiki/Juggler_(Trainer_class)"
                                                        title="Juggler (Trainer class)">Juggler (Trainer class)</a></li>
                                                <li><a href="/wiki/Junior_Representative_(Trainer_class)"
                                                        title="Junior Representative (Trainer class)">Junior
                                                        Representative (Trainer class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>K</h3>
                                            <ul>
                                                <li><a href="/wiki/Kantonian_Gym_(Trainer_class)"
                                                        title="Kantonian Gym (Trainer class)">Kantonian Gym (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Karate_Family_(Trainer_class)"
                                                        title="Karate Family (Trainer class)">Karate Family (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Kimono_Girl" title="Kimono Girl">Kimono Girl</a></li>
                                                <li><a href="/wiki/Kindler_(Trainer_class)"
                                                        title="Kindler (Trainer class)">Kindler (Trainer class)</a></li>
                                                <li><a href="/wiki/Kitakami_Ogre_Clan"
                                                        title="Kitakami Ogre Clan">Kitakami Ogre Clan</a></li>
                                                <li><a href="/wiki/Kruger_Family_(Trainer_class)"
                                                        title="Kruger Family (Trainer class)">Kruger Family (Trainer
                                                        class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>L</h3>
                                            <ul>
                                                <li><a href="/wiki/Lady_(Trainer_class)"
                                                        title="Lady (Trainer class)">Lady (Trainer class)</a></li>
                                                <li><a href="/wiki/Lady_in_Suit_(Trainer_class)"
                                                        title="Lady in Suit (Trainer class)">Lady in Suit (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Lass_(Trainer_class)"
                                                        title="Lass (Trainer class)">Lass (Trainer class)</a></li>
                                                <li><a href="/wiki/Leader-in-Training_(Trainer_class)"
                                                        title="Leader-in-Training (Trainer class)">Leader-in-Training
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/League_Club_(Trainer_class)"
                                                        title="League Club (Trainer class)">League Club (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/League_Staff_(Trainer_class)"
                                                        title="League Staff (Trainer class)">League Staff (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Linebacker_(Trainer_class)"
                                                        title="Linebacker (Trainer class)">Linebacker (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Lone_Wolf_(Trainer_class)"
                                                        title="Lone Wolf (Trainer class)">Lone Wolf (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Lumiose_Gang_Member_(Trainer_class)"
                                                        title="Lumiose Gang Member (Trainer class)">Lumiose Gang Member
                                                        (Trainer class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>M</h3>
                                            <ul>
                                                <li><a href="/wiki/Macro_Cosmos%27s_(Trainer_class)"
                                                        title="Macro Cosmos&#039;s (Trainer class)">Macro Cosmos&#039;s
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Madame_(Trainer_class)"
                                                        title="Madame (Trainer class)">Madame (Trainer class)</a></li>
                                                <li><a href="/wiki/Magician%27s_Apprentice_(Trainer_class)"
                                                        title="Magician&#039;s Apprentice (Trainer class)">Magician&#039;s
                                                        Apprentice (Trainer class)</a></li>
                                                <li><a href="/wiki/Magma_Admin_(Trainer_class)"
                                                        title="Magma Admin (Trainer class)">Magma Admin (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Maid_(Trainer_class)"
                                                        title="Maid (Trainer class)">Maid (Trainer class)</a></li>
                                                <li><a href="/wiki/Marchioness_(Trainer_class)"
                                                        title="Marchioness (Trainer class)">Marchioness (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Marquis_(Trainer_class)"
                                                        title="Marquis (Trainer class)">Marquis (Trainer class)</a></li>
                                                <li><a href="/wiki/Masked_Man_(Trainer_class)"
                                                        title="Masked Man (Trainer class)">Masked Man (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Masked_Woman_(Trainer_class)"
                                                        title="Masked Woman (Trainer class)">Masked Woman (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Master_%26_Apprentice_(Trainer_class)"
                                                        title="Master &amp; Apprentice (Trainer class)">Master &amp;
                                                        Apprentice (Trainer class)</a></li>
                                                <li><a href="/wiki/Master_Class_(Trainer_class)"
                                                        title="Master Class (Trainer class)">Master Class (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Master_Dojo_Student_(Trainer_class)"
                                                        title="Master Dojo Student (Trainer class)">Master Dojo Student
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Master_Representative_(Trainer_class)"
                                                        title="Master Representative (Trainer class)">Master
                                                        Representative (Trainer class)</a></li>
                                                <li><a href="/wiki/Matron_(Trainer_class)"
                                                        title="Matron (Trainer class)">Matron (Trainer class)</a></li>
                                                <li><a href="/wiki/Mature_Couple_(Trainer_class)"
                                                        title="Mature Couple (Trainer class)">Mature Couple (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/May-December_Couple_(Trainer_class)"
                                                        title="May-December Couple (Trainer class)">May-December Couple
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Medical_Team_(Trainer_class)"
                                                        title="Medical Team (Trainer class)">Medical Team (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Medium_(Trainer_class)"
                                                        title="Medium (Trainer class)">Medium (Trainer class)</a></li>
                                                <li><a href="/wiki/Miror_B.Peon_(Trainer_class)"
                                                        title="Miror B.Peon (Trainer class)">Miror B.Peon (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Model_(Trainer_class)"
                                                        title="Model (Trainer class)">Model (Trainer class)</a></li>
                                                <li><a href="/wiki/Monsieur_(Trainer_class)"
                                                        title="Monsieur (Trainer class)">Monsieur (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Movie_Star_(Trainer_class)"
                                                        title="Movie Star (Trainer class)">Movie Star (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Mt_BtlMaster_(Trainer_class)"
                                                        title="Mt BtlMaster (Trainer class)">Mt BtlMaster (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Muddy_Boy_(Trainer_class)"
                                                        title="Muddy Boy (Trainer class)">Muddy Boy (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Music_Crew_(Trainer_class)"
                                                        title="Music Crew (Trainer class)">Music Crew (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Musician_(Trainer_class)"
                                                        title="Musician (Trainer class)">Musician (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/Mysterious_Sisters_(Trainer_class)"
                                                        title="Mysterious Sisters (Trainer class)">Mysterious Sisters
                                                        (Trainer class)</a></li>
                                                <li><a href="/wiki/Mystery_Man_(Trainer_class)"
                                                        title="Mystery Man (Trainer class)">Mystery Man (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/Myth_Trainer_(Trainer_class)"
                                                        title="Myth Trainer (Trainer class)">Myth Trainer (Trainer
                                                        class)</a></li>
                                            </ul>
                                        </div>
                                        <div class="mw-category-group">
                                            <h3>N</h3>
                                            <ul>
                                                <li><a href="/wiki/Navigator_(Trainer_class)"
                                                        title="Navigator (Trainer class)">Navigator (Trainer class)</a>
                                                </li>
                                                <li><a href="/wiki/New_Actress_(Trainer_class)"
                                                        title="New Actress (Trainer class)">New Actress (Trainer
                                                        class)</a></li>
                                                <li><a href="/wiki/New_Star_(Trainer_class)"
                                                        title="New Star (Trainer class)">New Star (Trainer class)</a>
                                                </li>
                                            </ul>
                                        </div>
"""
import re

soup = BeautifulSoup(html.replace('\n',''), 'html.parser')
li_elements = soup.find_all('li')

with open('trainers.txt', 'w') as f:
    for li in li_elements:
        a_element = li.find('a')
        if a_element:
            trainer_name = a_element.text.split('(')[0].strip()
            trainer_name = re.sub(r'\s+', ' ', trainer_name)
            f.write(trainer_name + '\n')
