"""
Sample film data for initializing the vector database
"""

FILMS_DATA = [
    {
        "title": "back to the future",
        "description": "Cult science-fiction film from 1985 about Marty McFly, a teenager who accidentally travels thirty years into the past thanks to a modified DeLorean built by Dr. Emmett Brown, an eccentric scientist. Time-travel adventure with a futuristic car, temporal paradoxes, and a return to the future. Adventure comedy with special effects that were groundbreaking for the era.",
        "image_url": "/static/images/back-to-the-future.svg"
    },
    {
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "description": "Epic fantasy film from 2001 adapted from J.R.R. Tolkien’s novel. Frodo Baggins, a young hobbit, inherits a powerful and dangerous magical ring. He must embark on a long, perilous journey to destroy the One Ring in the fires of Mount Doom. Fantastic adventure with magic, mythical creatures, elves, dwarves, orcs, and an epic quest. First installment of The Lord of the Rings trilogy.",
        "image_url": "/static/images/lord-of-the-rings.svg"
    },
    {
        "title": "Inception",
        "description": "Psychological science-fiction thriller from 2010 directed by Christopher Nolan. Dom Cobb is a thief who specializes in extracting secrets by entering people’s dreams. He is offered a chance at redemption by doing the opposite: planting an idea in someone’s mind. Dream manipulation, reality vs. illusion, mind-bending architecture, and exploration of the depths of the unconscious. A complex film about dreams and the perception of reality.",
        "image_url": "/static/images/inception.svg"
    },
    {
        "title": "The Dark Knight",
        "description": "Dark, psychological superhero film from 2008 directed by Christopher Nolan. Batman faces the Joker, an anarchic criminal who plunges Gotham City into chaos. Exploration of themes of good and evil, justice and anarchy. Heath Ledger delivers a legendary performance as the Joker. Action film with spectacular set pieces and rare psychological depth for the superhero genre.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Pulp Fiction",
        "description": "Cult film from 1994 directed by Quentin Tarantino. A non-linear narrative following several crime-linked characters in Los Angeles. Vincent Vega and Jules Winnfield are hitmen, Butch Coolidge is a boxer, and Mia Wallace is the boss’s wife. Brilliant dialogue, stylized violence, and a revolutionary narrative structure. An independent film that redefined 1990s cinema.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Forrest Gump",
        "description": "Comedy-drama from 1994 starring Tom Hanks. Forrest Gump, a simple-minded but kind-hearted man, lives extraordinary adventures across American history from the 1950s to the 1980s. He meets Elvis Presley, fights in the Vietnam War, becomes a ping-pong champion, and builds a shrimp business. A touching film about innocence, love, and destiny.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "The Matrix",
        "description": "Revolutionary science-fiction film from 1999 directed by the Wachowskis. Neo, a computer programmer, discovers that reality is only a simulation created by intelligent machines. He joins a group of rebels led by Morpheus to free humanity from the Matrix. Groundbreaking visual effects, a deep philosophy about reality and freedom, and spectacular martial-arts fights.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Titanic",
        "description": "Romantic and dramatic epic from 1997 directed by James Cameron. Rose, a young aristocrat, falls in love with Jack, a poor artist, aboard the Titanic during its maiden voyage in 1912. Their love story unfolds amid the ship’s tragic sinking. Epic film with spectacular special effects, a heartbreaking romance, and an impressive historical recreation of the maritime disaster.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Avatar",
        "description": "Science-fiction epic from 2009 directed by James Cameron. Jake Sully, a paraplegic marine, is sent to Pandora, a distant moon, to infiltrate the Na’vi, an indigenous people. Through Avatar technology, he controls a Na’vi body and falls in love with Neytiri. A groundbreaking film with spectacular 3D visuals, a rich and detailed alien world, and ecological and anti-colonialist themes.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Interstellar",
        "description": "Epic science-fiction film from 2014 directed by Christopher Nolan. In a future where Earth becomes uninhabitable, a group of astronauts travels through a wormhole to find a new habitable planet. Cooper, a former pilot, must leave his family to save humanity. Exploration of time relativity, black holes, and love transcending dimensions. Visually stunning film with an emotional soundtrack.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "La La Land",
        "description": "Romantic musical comedy from 2016 directed by Damien Chazelle. Mia, an aspiring actress, and Sebastian, a jazz pianist, fall in love in Los Angeles while pursuing their artistic dreams. A modern musical with spectacular dance numbers, an enchanting jazz score, and a reflection on the sacrifices needed to achieve ambition. A homage to classic Hollywood cinema.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Parasite",
        "description": "Korean social thriller from 2019 directed by Bong Joon-ho. The Kim family, living in poverty, gradually infiltrates the wealthy Park family by posing as qualified employees. An acclaimed film exploring social inequality, capitalism, and class relations. A unique blend of dark comedy, psychological thriller, and social critique. The first non-English-language film to win the Academy Award for Best Picture.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Blade Runner",
        "description": "Neo-noir science-fiction film from 1982 directed by Ridley Scott. Rick Deckard, a detective tasked with retiring replicants, must hunt down four rogue androids in a dystopian Los Angeles of 2019. Explores themes of humanity, memory, and identity. Revolutionary visual aesthetic with a dark, melancholic cyberpunk atmosphere. A cult classic that influenced modern science fiction.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Casablanca",
        "description": "Classic romantic drama from 1942 directed by Michael Curtiz. Rick Blaine, a nightclub owner in Casablanca during World War II, must choose between love and duty when his former lover Ilsa reappears with her resistance-leader husband. Timeless film starring Humphrey Bogart and Ingrid Bergman. Memorable dialogue, moving romance, and themes of sacrifice and honor during wartime.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Citizen Kane",
        "description": "Biographical drama from 1941 directed by Orson Welles. The story of newspaper magnate Charles Foster Kane, told through flashbacks after his death. A revolutionary film in cinematic technique, with innovations in deep focus, lighting, and editing. Considered one of the greatest films in cinema history. Explores the corruption of power and the loneliness of wealth.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "The Godfather",
        "description": "Epic crime drama from 1972 directed by Francis Ford Coppola. The story of the Corleone family, an Italian-American Mafia dynasty. Michael Corleone, son of patriarch Vito, is drawn into the family’s criminal world. Masterful film with Marlon Brando and Al Pacino. Explores family, power, corruption, and the transformation of an innocent man into a Mafia boss.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Schindler's List",
        "description": "Historical drama from 1993 directed by Steven Spielberg. The true story of Oskar Schindler, a German industrialist who saved more than 1,000 Jews during the Holocaust by employing them in his factories. Shot in black and white with symbolic moments of color. A powerful portrait of humanity in the face of horror, redemption, and courage against injustice. A harrowing film about the Holocaust and resistance.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Goodfellas",
        "description": "Crime drama from 1990 directed by Martin Scorsese. The story of Henry Hill, an Italian-American gangster rising through the ranks of the New York Mafia. Based on a true story and starring Robert De Niro, Ray Liotta, and Joe Pesci. Explores organized crime, violence, and betrayal. Virtuosic direction with iconic long takes and a classic rock soundtrack.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "The Shawshank Redemption",
        "description": "Prison drama from 1994 directed by Frank Darabont. Andy Dufresne, a banker sentenced to life for murdering his wife, adapts to prison life and befriends Red. A film about hope, friendship, and redemption within the brutal prison world. Adapted from a Stephen King novella starring Tim Robbins and Morgan Freeman. A moving story of resilience and freedom.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Fight Club",
        "description": "Psychological drama from 1999 directed by David Fincher. An insomniac office worker creates an underground fight club with a charismatic soap salesman. A subversive film about masculinity, consumerism, and identity in modern society. Brad Pitt and Edward Norton in unforgettable roles. A biting critique of capitalism and social conformity with brutal fight scenes.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "The Silence of the Lambs",
        "description": "Psychological thriller from 1991 directed by Jonathan Demme. Clarice Starling, a young FBI trainee, must interview Hannibal Lecter, an imprisoned cannibal psychiatrist, to catch a serial killer. Anthony Hopkins gives a terrifying performance as Dr. Lecter. A film about criminal psychology, manipulation, and courage in the face of evil. An intense thriller with iconic scenes.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Gladiator",
        "description": "Historical epic from 2000 directed by Ridley Scott. Maximus, a betrayed Roman general turned slave, becomes a gladiator and seeks revenge against Emperor Commodus, who murdered his family. Russell Crowe delivers a powerful performance. Epic film with spectacular gladiator battles, impressive recreation of ancient Rome, and themes of vengeance and honor.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Saving Private Ryan",
        "description": "War film from 1998 directed by Steven Spielberg. A group of American soldiers is sent behind enemy lines to find and bring home Private Ryan, whose three brothers have been killed in action. Features a stunning opening depiction of the D-Day landings in Normandy. A realistic film about war, friendship, and sacrifice, starring Tom Hanks.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "The Lion King",
        "description": "Animated musical film from 1994 by Disney. Simba, a young lion prince, must overcome his uncle Scar’s betrayal and reclaim his rightful place as king of the savanna. Revolutionary animation with memorable songs by Elton John. Inspired by Shakespeare’s Hamlet. A moving film about family, responsibility, and the circle of life with unforgettable characters.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Toy Story",
        "description": "Animated film from 1995 produced by Pixar. Woody, a cowboy doll, sees his status as favorite toy threatened by the arrival of Buzz Lightyear, a high-tech astronaut. The first fully computer-animated feature film. A groundbreaking story about friendship, jealousy, and accepting change. Innovative animation with lovable characters and a universal story.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Jurassic Park",
        "description": "Science-fiction adventure film from 1993 directed by Steven Spielberg. A dinosaur theme park built on cloning turns into a nightmare when the creatures escape. Revolutionary CGI special effects. Adapted from Michael Crichton’s novel and starring Sam Neill, Laura Dern, and Jeff Goldblum. A thrilling adventure about the dangers of science and nature.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Terminator 2: Judgment Day",
        "description": "Science-fiction action film from 1991 directed by James Cameron. Sarah Connor and her son John are protected by a reprogrammed Terminator against a newer, more advanced model. Arnold Schwarzenegger in an iconic role. A revolutionary action film with spectacular effects. Explores themes of artificial intelligence, fate, and family protection.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Alien",
        "description": "Science-fiction horror film from 1979 directed by Ridley Scott. The crew of the spaceship Nostromo discovers a deadly extraterrestrial creature on a distant planet. Sigourney Weaver stars as the iconic Ripley. A dark, claustrophobic sci-fi film that uniquely blends science fiction and horror with an oppressive atmosphere and terrifying creatures.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Back to the Future Part II",
        "description": "Science-fiction film from 1989 directed by Robert Zemeckis. Marty McFly and Doc Brown travel to the future of 2015, then back to 1955 to fix temporal problems. Sequel to the cult classic starring Michael J. Fox and Christopher Lloyd. A complex exploration of time-travel paradoxes and consequences, with innovative special effects.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Indiana Jones and the Raiders of the Lost Ark",
        "description": "Adventure film from 1981 directed by Steven Spielberg. Indiana Jones, an archaeologist-adventurer, races to find the Ark of the Covenant before the Nazis. Harrison Ford in an iconic role. A classic adventure with unforgettable action scenes, mixing archaeology, mystery, and John Williams’s epic score.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "E.T. the Extra-Terrestrial",
        "description": "Family science-fiction film from 1982 directed by Steven Spielberg. A young boy named Elliott befriends a stranded alien and helps him return home. A touching film about friendship, family, and accepting difference. Henry Thomas and Drew Barrymore in memorable roles. An emotional family film with universal themes of love and compassion.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Ghostbusters",
        "description": "Science-fiction comedy from 1984 directed by Ivan Reitman. Three unemployed scientists start a ghost-catching business in New York City. Bill Murray, Dan Aykroyd, and Harold Ramis in iconic comedic roles. A cult classic with innovative effects and an unforgettable theme song. A supernatural comedy mixing humor and the paranormal with lovable characters.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Top Gun",
        "description": "Action film from 1986 directed by Tony Scott. Pete “Maverick” Mitchell, a talented but reckless fighter pilot, joins the elite Top Gun school. Tom Cruise in an iconic role. High-octane flight scenes and an energetic rock soundtrack. A portrait of the U.S. military elite with themes of competition, friendship, and romance.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Die Hard",
        "description": "Action film from 1988 directed by John McTiernan. John McClane, a New York cop, single-handedly takes on terrorists holding a Los Angeles skyscraper hostage. Bruce Willis in an iconic role. A genre-defining action classic blending suspense, humor, and a vulnerable, relatable hero.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "The Princess Bride",
        "description": "Romantic adventure film from 1987 directed by Rob Reiner. A love story between Westley and Buttercup, interrupted by pirates, giants, and evil princes. Cult classic starring Cary Elwes, Robin Wright, and André the Giant. A unique blend of adventure, romance, and comedy. A timeless family film with memorable characters and quotable lines.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Groundhog Day",
        "description": "Fantasy comedy from 1993 directed by Harold Ramis. Phil Connors, a cynical weatherman, finds himself trapped in a time loop reliving the same day over and over. Bill Murray in a standout comedic role. A film about redemption, love, and personal transformation. A philosophical comedy exploring time, fate, and self-improvement.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "The Big Lebowski",
        "description": "Dark comedy from 1998 directed by the Coen brothers. The Dude, a laid-back bowling enthusiast, gets caught up in a kidnapping case after being mistaken for a wealthy namesake. Jeff Bridges in an iconic role. A cult film with eccentric characters and memorable dialogue. An absurd comedy about misunderstandings, friendship, and a relaxed life philosophy.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Pulp Fiction",
        "description": "Cult film from 1994 directed by Quentin Tarantino. A non-linear narrative following several crime-linked characters in Los Angeles. Vincent Vega and Jules Winnfield are hitmen, Butch Coolidge is a boxer, and Mia Wallace is the boss’s wife. Brilliant dialogue, stylized violence, and a revolutionary narrative structure. An independent film that redefined 1990s cinema.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "The Usual Suspects",
        "description": "Crime thriller from 1995 directed by Bryan Singer. Five criminals are brought together for a heist, but things go wrong and reveal the existence of a mysterious mastermind named Keyser Söze. Kevin Spacey in a memorable role. A film with a legendary final twist. A complex psychological thriller about manipulation, memory, and truth, with an ingenious narrative structure.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Se7en",
        "description": "Psychological thriller from 1995 directed by David Fincher. Two detectives hunt a serial killer who bases murders on the seven deadly sins. Brad Pitt and Morgan Freeman in memorable roles. A bleak, rain-soaked film with a desperate atmosphere. An intense thriller about evil, justice, and the corruption of the human soul.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "The Sixth Sense",
        "description": "Psychological thriller from 1999 directed by M. Night Shyamalan. Malcolm Crowe, a child psychologist, treats a young boy who claims to see dead people. Bruce Willis and Haley Joel Osment in memorable roles. A film with a legendary final twist. A psychological thriller about perception, truth, and acceptance, ending with a shocking revelation.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Memento",
        "description": "Psychological thriller from 2000 directed by Christopher Nolan. Leonard, a man suffering from anterograde amnesia, searches for his wife’s killer using notes and tattoos. Guy Pearce in a complex role. A film with a revolutionary backwards-told structure. A psychological thriller about memory, identity, and truth with a unique narrative approach.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Donnie Darko",
        "description": "Psychological science-fiction film from 2001 directed by Richard Kelly. Donnie, a troubled teenager, sees a giant rabbit who predicts the end of the world in 28 days. Jake Gyllenhaal in a memorable role. A cult film blending science fiction, psychology, and philosophy. Explores time, fate, and reality with a dreamlike, unsettling atmosphere.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Eternal Sunshine of the Spotless Mind",
        "description": "Romantic science-fiction film from 2004 directed by Michel Gondry. After a painful breakup, Joel and Clementine erase each other from their memories. Jim Carrey and Kate Winslet in dramatic roles. A film about love, memory, and human relationships. A poetic exploration of heartbreak and the importance of memories—even painful ones.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "No Country for Old Men",
        "description": "Thriller from 2007 directed by the Coen brothers. Llewelyn Moss finds a bag of money after a drug deal goes wrong, but is pursued by a psychopathic killer. Javier Bardem in a terrifying role. A dark, violent film about fate, morality, and violence. An intense psychological thriller with an oppressive atmosphere and complex characters.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "There Will Be Blood",
        "description": "Historical drama from 2007 directed by Paul Thomas Anderson. Daniel Plainview, a ruthless oil prospector, builds an oil empire in the early 20th century. Daniel Day-Lewis in an Oscar-winning performance. A film about ambition, greed, and the corruption of capitalism. An intense psychological drama about the thirst for power and the destruction of the human soul.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "The Social Network",
        "description": "Biographical drama from 2010 directed by David Fincher. The story of Facebook’s creation by Mark Zuckerberg and the legal conflicts that followed. Jesse Eisenberg plays Zuckerberg. A film about innovation, friendship, and the consequences of success. A modern portrait of tech entrepreneurship with themes of betrayal and ambition.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Mad Max: Fury Road",
        "description": "Post-apocalyptic action film from 2015 directed by George Miller. Max and Furiosa flee a tyrant in a desert world ravaged by war. Tom Hardy and Charlize Theron in standout roles. A revolutionary action film featuring spectacular car chases. Pure action with themes of freedom, survival, and redemption in a post-apocalyptic world.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Get Out",
        "description": "Psychological horror thriller from 2017 directed by Jordan Peele. Chris, a Black photographer, visits his girlfriend’s white family and uncovers a terrifying secret. Daniel Kaluuya in a memorable role. A film about racism, manipulation, and social horror. A smart psychological thriller blending horror and social critique in a unique, hard-hitting way.",
        "image_url": "/static/images/film-placeholder.svg"
    },
    {
        "title": "Joker",
        "description": "Psychological drama from 2019 directed by Todd Phillips. Arthur Fleck, a failed comedian with mental health struggles, descends into madness and becomes the Joker. Joaquin Phoenix in an Oscar-winning performance. A dark film about mental illness, social exclusion, and violence. A disturbing psychological portrait of a man broken by society, with themes of revolt and insanity.",
        "image_url": "/static/images/film-placeholder.svg"
    }
]
