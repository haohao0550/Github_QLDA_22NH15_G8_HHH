from django.core.management.base import BaseCommand
from vocabulary.models import Topic, Vocabulary
import random

class Command(BaseCommand):
    help = 'Load sample topics and vocabulary data'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')
        
        # Clear existing data
        Vocabulary.objects.all().delete()
        Topic.objects.all().delete()
        
        # Sample data structure
        topics_data = {
            "Animals & Wildlife": {
                "description": "Learn vocabulary about animals, pets, and wildlife from around the world",
                "color": "#10B981",
                "vocabulary": [
                    {"word": "Elephant", "pronunciation": "/ˈɛlɪfənt/", "meaning": "A very large mammal with a trunk, large ears, and tusks", "example": "The elephant is the largest land animal in the world.", "difficulty": "easy"},
                    {"word": "Butterfly", "pronunciation": "/ˈbʌtərflaɪ/", "meaning": "A flying insect with large colorful wings", "example": "The butterfly landed gently on the flower.", "difficulty": "easy"},
                    {"word": "Rhinoceros", "pronunciation": "/raɪˈnɒsərəs/", "meaning": "A large thick-skinned mammal with one or two horns on the nose", "example": "The rhinoceros is an endangered species in many parts of Africa.", "difficulty": "hard"},
                    {"word": "Penguin", "pronunciation": "/ˈpɛŋɡwɪn/", "meaning": "A flightless seabird with black and white plumage", "example": "Penguins are excellent swimmers despite being unable to fly.", "difficulty": "medium"},
                    {"word": "Giraffe", "pronunciation": "/dʒɪˈræf/", "meaning": "A tall African mammal with a very long neck and legs", "example": "The giraffe can reach leaves high up in the trees.", "difficulty": "easy"},
                    {"word": "Chimpanzee", "pronunciation": "/ˌtʃɪmpænˈziː/", "meaning": "A great ape that lives in forests of tropical Africa", "example": "Chimpanzees are our closest living relatives in the animal kingdom.", "difficulty": "medium"},
                    {"word": "Kangaroo", "pronunciation": "/ˌkæŋɡəˈruː/", "meaning": "A large marsupial from Australia that hops on its hind legs", "example": "The kangaroo carries its baby in a pouch.", "difficulty": "medium"},
                    {"word": "Octopus", "pronunciation": "/ˈɒktəpəs/", "meaning": "A sea creature with eight arms and a soft body", "example": "The octopus can change its color to blend with its surroundings.", "difficulty": "medium"},
                    {"word": "Leopard", "pronunciation": "/ˈlɛpərd/", "meaning": "A large wild cat with a spotted coat", "example": "The leopard is known for its incredible climbing abilities.", "difficulty": "medium"},
                    {"word": "Dolphin", "pronunciation": "/ˈdɒlfɪn/", "meaning": "A highly intelligent marine mammal", "example": "Dolphins communicate with each other using clicks and whistles.", "difficulty": "easy"},
                    {"word": "Crocodile", "pronunciation": "/ˈkrɒkədaɪl/", "meaning": "A large reptile with powerful jaws that lives in water", "example": "The crocodile waited patiently for its prey by the riverbank.", "difficulty": "medium"},
                    {"word": "Peacock", "pronunciation": "/ˈpiːkɒk/", "meaning": "A large bird with beautiful, colorful tail feathers", "example": "The male peacock displays its magnificent tail to attract females.", "difficulty": "easy"},
                    {"word": "Chameleon", "pronunciation": "/kəˈmiːliən/", "meaning": "A lizard that can change its skin color", "example": "The chameleon slowly changed from green to brown.", "difficulty": "hard"},
                    {"word": "Hummingbird", "pronunciation": "/ˈhʌmɪŋbɜːrd/", "meaning": "A very small bird that can hover in the air", "example": "The hummingbird's wings beat so fast they create a humming sound.", "difficulty": "medium"},
                    {"word": "Porcupine", "pronunciation": "/ˈpɔːrkjupaɪn/", "meaning": "A rodent covered with sharp spines or quills", "example": "The porcupine raises its quills when it feels threatened.", "difficulty": "hard"},
                    {"word": "Flamingo", "pronunciation": "/fləˈmɪŋɡoʊ/", "meaning": "A large pink or red bird with long legs and neck", "example": "Flamingos get their pink color from the food they eat.", "difficulty": "medium"},
                    {"word": "Cheetah", "pronunciation": "/ˈtʃiːtə/", "meaning": "The fastest land animal, a spotted wild cat", "example": "The cheetah can run up to 70 miles per hour.", "difficulty": "easy"},
                    {"word": "Walrus", "pronunciation": "/ˈwɔːlrəs/", "meaning": "A large marine mammal with tusks", "example": "The walrus uses its tusks to pull itself out of the water.", "difficulty": "medium"},
                    {"word": "Mongoose", "pronunciation": "/ˈmɒŋɡuːs/", "meaning": "A small carnivorous mammal known for fighting snakes", "example": "The mongoose is famous for its ability to kill venomous snakes.", "difficulty": "hard"},
                    {"word": "Platypus", "pronunciation": "/ˈplætɪpəs/", "meaning": "An unusual Australian mammal that lays eggs", "example": "The platypus is one of the few mammals that lay eggs instead of giving birth.", "difficulty": "hard"}
                ]
            },
            
            "Food & Cooking": {
                "description": "Vocabulary related to food, cooking, restaurants, and culinary arts",
                "color": "#F59E0B",
                "vocabulary": [
                    {"word": "Cuisine", "pronunciation": "/kwɪˈziːn/", "meaning": "A style or method of cooking, especially as characteristic of a particular country", "example": "Italian cuisine is famous for its pasta and pizza dishes.", "difficulty": "medium"},
                    {"word": "Appetizer", "pronunciation": "/ˈæpɪtaɪzər/", "meaning": "A small dish of food served before the main course", "example": "We ordered bruschetta as an appetizer before our main meal.", "difficulty": "medium"},
                    {"word": "Delicious", "pronunciation": "/dɪˈlɪʃəs/", "meaning": "Having a very pleasant taste or smell", "example": "The homemade chocolate cake was absolutely delicious.", "difficulty": "easy"},
                    {"word": "Marinate", "pronunciation": "/ˈmærɪneɪt/", "meaning": "To soak food in a seasoned liquid before cooking", "example": "You should marinate the chicken for at least two hours before grilling.", "difficulty": "hard"},
                    {"word": "Sauté", "pronunciation": "/sɔːˈteɪ/", "meaning": "To fry quickly in a little hot fat", "example": "Sauté the onions until they become golden brown.", "difficulty": "hard"},
                    {"word": "Garnish", "pronunciation": "/ˈɡɑːrnɪʃ/", "meaning": "A decoration or embellishment for food", "example": "The chef added a sprig of parsley as a garnish.", "difficulty": "medium"},
                    {"word": "Ingredient", "pronunciation": "/ɪnˈɡriːdiənt/", "meaning": "Any of the foods or substances that are combined to make a particular dish", "example": "Fresh herbs are an essential ingredient in this recipe.", "difficulty": "easy"},
                    {"word": "Recipe", "pronunciation": "/ˈrɛsəpi/", "meaning": "A set of instructions for preparing a particular dish", "example": "I found this recipe for chocolate chip cookies online.", "difficulty": "easy"},
                    {"word": "Seasoning", "pronunciation": "/ˈsiːzənɪŋ/", "meaning": "Salt, herbs, or spices added to food to enhance flavor", "example": "This soup needs more seasoning to taste better.", "difficulty": "medium"},
                    {"word": "Tender", "pronunciation": "/ˈtɛndər/", "meaning": "Easy to cut or chew; not tough", "example": "The meat was so tender it fell off the bone.", "difficulty": "easy"},
                    {"word": "Crispy", "pronunciation": "/ˈkrɪspi/", "meaning": "Hard and brittle; making a sharp cracking sound when bitten", "example": "I love crispy bacon with my breakfast.", "difficulty": "easy"},
                    {"word": "Simmer", "pronunciation": "/ˈsɪmər/", "meaning": "To cook gently at a temperature just below boiling", "example": "Let the sauce simmer for 20 minutes to develop the flavors.", "difficulty": "medium"},
                    {"word": "Whisk", "pronunciation": "/wɪsk/", "meaning": "To beat or stir with a light, rapid movement", "example": "Whisk the eggs until they are light and fluffy.", "difficulty": "medium"},
                    {"word": "Gourmet", "pronunciation": "/ɡʊrˈmeɪ/", "meaning": "High-quality food; a connoisseur of fine food", "example": "This restaurant serves gourmet meals prepared by expert chefs.", "difficulty": "hard"},
                    {"word": "Savory", "pronunciation": "/ˈseɪvəri/", "meaning": "Having a pleasant taste or smell; not sweet", "example": "I prefer savory snacks over sweet ones.", "difficulty": "medium"},
                    {"word": "Bland", "pronunciation": "/blænd/", "meaning": "Lacking strong features or characteristics; not interesting", "example": "The soup was too bland and needed more spices.", "difficulty": "medium"},
                    {"word": "Spicy", "pronunciation": "/ˈspaɪsi/", "meaning": "Flavored with or containing strong spices", "example": "This curry is too spicy for me to eat.", "difficulty": "easy"},
                    {"word": "Nutritious", "pronunciation": "/nuˈtrɪʃəs/", "meaning": "Containing substances necessary for growth, health, and good condition", "example": "Vegetables are nutritious and should be part of every meal.", "difficulty": "medium"},
                    {"word": "Organic", "pronunciation": "/ɔːrˈɡænɪk/", "meaning": "Produced without using artificial chemicals", "example": "We only buy organic fruits and vegetables.", "difficulty": "medium"},
                    {"word": "Fermented", "pronunciation": "/fərˈmɛntɪd/", "meaning": "Having undergone fermentation", "example": "Fermented foods like yogurt are good for digestion.", "difficulty": "hard"}
                ]
            },
            
            "Technology & Innovation": {
                "description": "Modern technology, gadgets, software, and digital innovation terms",
                "color": "#3B82F6",
                "vocabulary": [
                    {"word": "Algorithm", "pronunciation": "/ˈælɡərɪðəm/", "meaning": "A set of rules or instructions for solving a problem", "example": "The search algorithm helps users find relevant information quickly.", "difficulty": "hard"},
                    {"word": "Software", "pronunciation": "/ˈsɔːftwɛər/", "meaning": "Computer programs and applications", "example": "The company develops software for mobile applications.", "difficulty": "medium"},
                    {"word": "Download", "pronunciation": "/ˈdaʊnloʊd/", "meaning": "To transfer data from a remote computer to a local device", "example": "Please download the latest version of the app from the store.", "difficulty": "easy"},
                    {"word": "Cybersecurity", "pronunciation": "/ˈsaɪbərsɪˌkjʊrɪti/", "meaning": "The practice of protecting systems and data from digital attacks", "example": "Cybersecurity is crucial for protecting sensitive business information.", "difficulty": "hard"},
                    {"word": "Artificial Intelligence", "pronunciation": "/ˌɑːrtɪˈfɪʃəl ɪnˈtɛlɪdʒəns/", "meaning": "Computer systems able to perform tasks that typically require human intelligence", "example": "Artificial intelligence is revolutionizing many industries.", "difficulty": "hard"},
                    {"word": "Cloud Computing", "pronunciation": "/klaʊd kəmˈpjuːtɪŋ/", "meaning": "The delivery of computing services over the internet", "example": "Cloud computing allows us to access our files from anywhere.", "difficulty": "medium"},
                    {"word": "Database", "pronunciation": "/ˈdeɪtəbeɪs/", "meaning": "A structured collection of data", "example": "The customer information is stored in our database.", "difficulty": "medium"},
                    {"word": "Interface", "pronunciation": "/ˈɪntərfeɪs/", "meaning": "A point where two systems meet and interact", "example": "The user interface of this app is very intuitive.", "difficulty": "medium"},
                    {"word": "Bandwidth", "pronunciation": "/ˈbændwɪdθ/", "meaning": "The maximum rate of data transfer across a network", "example": "We need more bandwidth to handle the increased internet traffic.", "difficulty": "hard"},
                    {"word": "Encryption", "pronunciation": "/ɪnˈkrɪpʃən/", "meaning": "The process of converting information into a secret code", "example": "Encryption protects your personal data from hackers.", "difficulty": "hard"},
                    {"word": "Smartphone", "pronunciation": "/ˈsmɑːrtfoʊn/", "meaning": "A mobile phone with advanced features", "example": "My smartphone has a great camera for taking photos.", "difficulty": "easy"},
                    {"word": "Application", "pronunciation": "/ˌæplɪˈkeɪʃən/", "meaning": "A computer program designed for end users", "example": "I downloaded a new application to track my fitness goals.", "difficulty": "easy"},
                    {"word": "Virtual Reality", "pronunciation": "/ˈvɜːrtʃuəl riˈæləti/", "meaning": "Computer-generated simulation of a three-dimensional environment", "example": "Virtual reality gaming provides an immersive experience.", "difficulty": "medium"},
                    {"word": "Blockchain", "pronunciation": "/ˈblɑːktʃeɪn/", "meaning": "A system of recording information in a way that makes it difficult to change", "example": "Blockchain technology is the foundation of cryptocurrency.", "difficulty": "hard"},
                    {"word": "Automation", "pronunciation": "/ˌɔːtəˈmeɪʃən/", "meaning": "The use of technology to perform tasks without human intervention", "example": "Automation has increased efficiency in manufacturing.", "difficulty": "medium"},
                    {"word": "Innovation", "pronunciation": "/ˌɪnəˈveɪʃən/", "meaning": "The introduction of new ideas, methods, or products", "example": "Innovation drives progress in the technology industry.", "difficulty": "medium"},
                    {"word": "Digital", "pronunciation": "/ˈdɪdʒɪtəl/", "meaning": "Relating to computer technology", "example": "We live in a digital age where everything is connected.", "difficulty": "easy"},
                    {"word": "Network", "pronunciation": "/ˈnɛtwɜːrk/", "meaning": "A group of interconnected computers or devices", "example": "The office network allows all employees to share files.", "difficulty": "easy"},
                    {"word": "Programming", "pronunciation": "/ˈproʊɡræmɪŋ/", "meaning": "The process of creating computer software", "example": "Learning programming opens up many career opportunities.", "difficulty": "medium"},
                    {"word": "Upgrade", "pronunciation": "/ˈʌpɡreɪd/", "meaning": "To improve or enhance something to a higher standard", "example": "I need to upgrade my computer to run the latest software.", "difficulty": "easy"}
                ]
            },
            
            "Travel & Transportation": {
                "description": "Words related to travel, transportation, hotels, and tourism",
                "color": "#8B5CF6",
                "vocabulary": [
                    {"word": "Destination", "pronunciation": "/ˌdɛstɪˈneɪʃən/", "meaning": "The place to which someone or something is going", "example": "Paris is a popular tourist destination.", "difficulty": "medium"},
                    {"word": "Itinerary", "pronunciation": "/aɪˈtɪnəˌrɛri/", "meaning": "A planned route or journey", "example": "Our travel itinerary includes visits to three different countries.", "difficulty": "hard"},
                    {"word": "Luggage", "pronunciation": "/ˈlʌɡɪdʒ/", "meaning": "Suitcases and bags containing personal belongings", "example": "Please keep your luggage with you at all times.", "difficulty": "easy"},
                    {"word": "Passport", "pronunciation": "/ˈpæspɔːrt/", "meaning": "An official document for international travel", "example": "Don't forget to bring your passport to the airport.", "difficulty": "easy"},
                    {"word": "Accommodation", "pronunciation": "/əˌkɑːməˈdeɪʃən/", "meaning": "A place where someone can stay", "example": "We booked accommodation near the beach for our vacation.", "difficulty": "medium"},
                    {"word": "Departure", "pronunciation": "/dɪˈpɑːrtʃər/", "meaning": "The action of leaving", "example": "The departure time for our flight is 3:00 PM.", "difficulty": "medium"},
                    {"word": "Arrival", "pronunciation": "/əˈraɪvəl/", "meaning": "The action of coming to a destination", "example": "We celebrated our safe arrival in Tokyo.", "difficulty": "easy"},
                    {"word": "Boarding", "pronunciation": "/ˈbɔːrdɪŋ/", "meaning": "Getting on a ship, aircraft, or other vehicle", "example": "Boarding for flight 123 will begin in 30 minutes.", "difficulty": "medium"},
                    {"word": "Terminal", "pronunciation": "/ˈtɜːrmɪnəl/", "meaning": "A building at an airport where passengers transfer", "example": "Our gate is located in Terminal 2.", "difficulty": "medium"},
                    {"word": "Customs", "pronunciation": "/ˈkʌstəmz/", "meaning": "The official department that administers duties on imported goods", "example": "We had to go through customs when we entered the country.", "difficulty": "medium"},
                    {"word": "Reservation", "pronunciation": "/ˌrɛzərˈveɪʃən/", "meaning": "An arrangement to have something kept for particular use", "example": "I made a reservation at the restaurant for tonight.", "difficulty": "medium"},
                    {"word": "Tourist", "pronunciation": "/ˈtʊrɪst/", "meaning": "A person who travels for pleasure", "example": "The city is full of tourists during the summer months.", "difficulty": "easy"},
                    {"word": "Sightseeing", "pronunciation": "/ˈsaɪtsiːɪŋ/", "meaning": "The activity of visiting places of interest", "example": "We spent the day sightseeing in the historic district.", "difficulty": "medium"},
                    {"word": "Excursion", "pronunciation": "/ɪkˈskɜːrʒən/", "meaning": "A short journey or trip for pleasure", "example": "We took an excursion to the nearby islands.", "difficulty": "hard"},
                    {"word": "Voyage", "pronunciation": "/ˈvɔɪɪdʒ/", "meaning": "A long journey involving travel by sea or in space", "example": "The voyage across the Atlantic took two weeks.", "difficulty": "medium"},
                    {"word": "Transit", "pronunciation": "/ˈtrænzɪt/", "meaning": "The carrying of people or things from one place to another", "example": "We have a two-hour transit in Amsterdam.", "difficulty": "medium"},
                    {"word": "Commute", "pronunciation": "/kəˈmjuːt/", "meaning": "Travel some distance between one's home and place of work", "example": "My daily commute to work takes about 45 minutes.", "difficulty": "medium"},
                    {"word": "Navigation", "pronunciation": "/ˌnævɪˈɡeɪʃən/", "meaning": "The process of planning and following a route", "example": "GPS navigation makes it easy to find your way in unfamiliar places.", "difficulty": "hard"},
                    {"word": "Journey", "pronunciation": "/ˈdʒɜːrni/", "meaning": "An act of traveling from one place to another", "example": "The journey to the mountain village was long but beautiful.", "difficulty": "easy"},
                    {"word": "Adventure", "pronunciation": "/ədˈvɛntʃər/", "meaning": "An unusual and exciting experience or activity", "example": "Our hiking trip turned into quite an adventure.", "difficulty": "easy"}
                ]
            },
            
            "Business & Finance": {
                "description": "Professional vocabulary for business, finance, and workplace communication",
                "color": "#EF4444",
                "vocabulary": [
                    {"word": "Investment", "pronunciation": "/ɪnˈvɛstmənt/", "meaning": "The action of investing money for profit", "example": "Real estate can be a good long-term investment.", "difficulty": "medium"},
                    {"word": "Revenue", "pronunciation": "/ˈrɛvəˌnu/", "meaning": "Income generated from business operations", "example": "The company's revenue increased by 15% this quarter.", "difficulty": "medium"},
                    {"word": "Profit", "pronunciation": "/ˈprɑːfɪt/", "meaning": "Financial gain from business activity", "example": "The business made a substantial profit last year.", "difficulty": "easy"},
                    {"word": "Budget", "pronunciation": "/ˈbʌdʒɪt/", "meaning": "An estimate of income and expenditure", "example": "We need to create a budget for the marketing campaign.", "difficulty": "easy"},
                    {"word": "Entrepreneur", "pronunciation": "/ˌɑːntrəprəˈnɜːr/", "meaning": "A person who starts and runs a business", "example": "She's a successful entrepreneur who built her company from scratch.", "difficulty": "hard"},
                    {"word": "Corporation", "pronunciation": "/ˌkɔːrpəˈreɪʃən/", "meaning": "A large business or organization", "example": "The corporation has offices in over 50 countries.", "difficulty": "medium"},
                    {"word": "Stakeholder", "pronunciation": "/ˈsteɪkhoʊldər/", "meaning": "A person with an interest in a business", "example": "We need to consider all stakeholders when making this decision.", "difficulty": "hard"},
                    {"word": "Marketing", "pronunciation": "/ˈmɑːrkɪtɪŋ/", "meaning": "The activity of promoting and selling products", "example": "Our marketing team developed a creative advertising campaign.", "difficulty": "easy"},
                    {"word": "Strategy", "pronunciation": "/ˈstrætədʒi/", "meaning": "A plan of action designed to achieve a goal", "example": "The company's growth strategy focuses on international expansion.", "difficulty": "medium"},
                    {"word": "Negotiation", "pronunciation": "/nɪˌɡoʊʃiˈeɪʃən/", "meaning": "Discussion aimed at reaching an agreement", "example": "The negotiation for the contract took several weeks.", "difficulty": "hard"},
                    {"word": "Productivity", "pronunciation": "/ˌproʊdʌkˈtɪvəti/", "meaning": "The effectiveness of productive effort", "example": "New software tools have improved our team's productivity.", "difficulty": "medium"},
                    {"word": "Efficiency", "pronunciation": "/ɪˈfɪʃənsi/", "meaning": "The ability to accomplish something with minimum waste", "example": "We're looking for ways to improve efficiency in our operations.", "difficulty": "medium"},
                    {"word": "Innovation", "pronunciation": "/ˌɪnəˈveɪʃən/", "meaning": "The introduction of new ideas or methods", "example": "Innovation is key to staying competitive in the market.", "difficulty": "medium"},
                    {"word": "Merger", "pronunciation": "/ˈmɜːrdʒər/", "meaning": "A combination of two companies into one", "example": "The merger created one of the largest companies in the industry.", "difficulty": "hard"},
                    {"word": "Acquisition", "pronunciation": "/ˌækwɪˈzɪʃən/", "meaning": "The buying of one company by another", "example": "The acquisition will help us expand into new markets.", "difficulty": "hard"},
                    {"word": "Dividend", "pronunciation": "/ˈdɪvɪdɛnd/", "meaning": "A payment made by a corporation to its shareholders", "example": "Shareholders received a dividend of $2 per share.", "difficulty": "hard"},
                    {"word": "Liability", "pronunciation": "/ˌlaɪəˈbɪləti/", "meaning": "The state of being responsible for something", "example": "The company's liabilities exceeded its assets.", "difficulty": "hard"},
                    {"word": "Asset", "pronunciation": "/ˈæsɛt/", "meaning": "A useful or valuable thing owned by a company", "example": "The building is the company's most valuable asset.", "difficulty": "medium"},
                    {"word": "Franchise", "pronunciation": "/ˈfræntʃaɪz/", "meaning": "A license to operate a business using another company's brand", "example": "He opened a franchise of the popular restaurant chain.", "difficulty": "medium"},
                    {"word": "Bankruptcy", "pronunciation": "/ˈbæŋkrʌptsi/", "meaning": "Legal status of being unable to repay debts", "example": "The company filed for bankruptcy after years of losses.", "difficulty": "hard"}
                ]
            },
            
            "Health & Medicine": {
                "description": "Medical terms, health conditions, and wellness vocabulary",
                "color": "#06B6D4",
                "vocabulary": [
                    {"word": "Diagnosis", "pronunciation": "/ˌdaɪəɡˈnoʊsɪs/", "meaning": "The identification of a disease or condition", "example": "The doctor's diagnosis was confirmed by the test results.", "difficulty": "medium"},
                    {"word": "Symptom", "pronunciation": "/ˈsɪmptəm/", "meaning": "A sign of disease or illness", "example": "Fever is a common symptom of the flu.", "difficulty": "easy"},
                    {"word": "Treatment", "pronunciation": "/ˈtriːtmənt/", "meaning": "Medical care for an illness or injury", "example": "The treatment for his condition was very effective.", "difficulty": "easy"},
                    {"word": "Prescription", "pronunciation": "/prɪˈskrɪpʃən/", "meaning": "A doctor's written order for medicine", "example": "I need to pick up my prescription from the pharmacy.", "difficulty": "medium"},
                    {"word": "Vaccination", "pronunciation": "/ˌvæksɪˈneɪʃən/", "meaning": "Treatment with a vaccine to produce immunity", "example": "Vaccination helps prevent serious diseases.", "difficulty": "medium"},
                    {"word": "Surgery", "pronunciation": "/ˈsɜːrdʒəri/", "meaning": "Medical treatment involving an operation", "example": "The patient recovered quickly after the surgery.", "difficulty": "easy"},
                    {"word": "Rehabilitation", "pronunciation": "/ˌriːhəˌbɪlɪˈteɪʃən/", "meaning": "The process of helping someone recover", "example": "Physical rehabilitation helped him walk again.", "difficulty": "hard"},
                    {"word": "Nutrition", "pronunciation": "/nuˈtrɪʃən/", "meaning": "The process of providing food necessary for health", "example": "Good nutrition is essential for maintaining health.", "difficulty": "medium"},
                    {"word": "Exercise", "pronunciation": "/ˈɛksərˌsaɪz/", "meaning": "Physical activity to improve health and fitness", "example": "Regular exercise can help prevent heart disease.", "difficulty": "easy"},
                    {"word": "Wellness", "pronunciation": "/ˈwɛlnəs/", "meaning": "The state of being in good health", "example": "The company promotes employee wellness through fitness programs.", "difficulty": "medium"},
                    {"word": "Immunity", "pronunciation": "/ɪˈmjuːnəti/", "meaning": "The ability to resist infection or disease", "example": "A healthy lifestyle can boost your immunity.", "difficulty": "medium"},
                    {"word": "Infection", "pronunciation": "/ɪnˈfɛkʃən/", "meaning": "The invasion of the body by harmful microorganisms", "example": "The wound became infected and needed antibiotic treatment.", "difficulty": "medium"},
                    {"word": "Antibiotic", "pronunciation": "/ˌæntibaɪˈɑːtɪk/", "meaning": "Medicine that destroys or inhibits bacteria", "example": "The doctor prescribed antibiotics to fight the infection.", "difficulty": "hard"},
                    {"word": "Chronic", "pronunciation": "/ˈkrɑːnɪk/", "meaning": "Persisting for a long time or constantly recurring", "example": "Diabetes is a chronic condition that requires ongoing management.", "difficulty": "hard"},
                    {"word": "Acute", "pronunciation": "/əˈkjuːt/", "meaning": "Severe or intense; having a rapid onset", "example": "The patient was admitted with acute chest pain.", "difficulty": "hard"},
                    {"word": "Prevention", "pronunciation": "/prɪˈvɛnʃən/", "meaning": "The action of stopping something from happening", "example": "Prevention is better than cure when it comes to health.", "difficulty": "medium"},
                    {"word": "Therapy", "pronunciation": "/ˈθɛrəpi/", "meaning": "Treatment intended to relieve or heal a disorder", "example": "Speech therapy helped the child improve communication skills.", "difficulty": "medium"},
                    {"word": "Epidemic", "pronunciation": "/ˌɛpɪˈdɛmɪk/", "meaning": "A widespread occurrence of disease", "example": "The flu epidemic affected thousands of people.", "difficulty": "hard"},
                    {"word": "Hygiene", "pronunciation": "/ˈhaɪdʒiːn/", "meaning": "Conditions or practices conducive to maintaining health", "example": "Good personal hygiene helps prevent the spread of germs.", "difficulty": "medium"},
                    {"word": "Metabolism", "pronunciation": "/məˈtæbəˌlɪzəm/", "meaning": "Chemical processes that occur within a living organism", "example": "Regular exercise can help boost your metabolism.", "difficulty": "hard"}
                ]
            },
            
            "Education & Learning": {
                "description": "Academic vocabulary, school subjects, and educational terms",
                "color": "#84CC16",
                "vocabulary": [
                    {"word": "Curriculum", "pronunciation": "/kəˈrɪkjələm/", "meaning": "The subjects comprising a course of study", "example": "The new curriculum includes more science and technology courses.", "difficulty": "medium"},
                    {"word": "Scholarship", "pronunciation": "/ˈskɑːlərʃɪp/", "meaning": "A grant of money for academic study", "example": "She received a scholarship to study at the university.", "difficulty": "medium"},
                    {"word": "Assignment", "pronunciation": "/əˈsaɪnmənt/", "meaning": "A task or piece of work given to students", "example": "The assignment is due next Friday.", "difficulty": "easy"},
                    {"word": "Research", "pronunciation": "/rɪˈsɜːrtʃ/", "meaning": "Detailed study of a subject to discover new information", "example": "His research on climate change was published in a scientific journal.", "difficulty": "medium"},
                    {"word": "Knowledge", "pronunciation": "/ˈnɑːlɪdʒ/", "meaning": "Facts, information, and skills acquired through experience", "example": "Knowledge is power in today's information age.", "difficulty": "easy"},
                    {"word": "Comprehension", "pronunciation": "/ˌkɑːmprɪˈhɛnʃən/", "meaning": "The ability to understand something", "example": "Reading comprehension is an important skill for students.", "difficulty": "medium"},
                    {"word": "Analysis", "pronunciation": "/əˈnæləsɪs/", "meaning": "Detailed examination of elements or structure", "example": "The analysis of the data revealed interesting patterns.", "difficulty": "medium"},
                    {"word": "Hypothesis", "pronunciation": "/haɪˈpɑːθəsɪs/", "meaning": "A proposed explanation for a phenomenon", "example": "The scientist tested her hypothesis through experiments.", "difficulty": "hard"},
                    {"word": "Methodology", "pronunciation": "/ˌmɛθəˈdɑːlədʒi/", "meaning": "A system of methods used in a particular area of study", "example": "The research methodology was carefully designed to ensure accurate results.", "difficulty": "hard"},
                    {"word": "Evaluation", "pronunciation": "/ɪˌvæljuˈeɪʃən/", "meaning": "The making of a judgment about the value of something", "example": "The teacher's evaluation of the project was very positive.", "difficulty": "medium"},
                    {"word": "Literacy", "pronunciation": "/ˈlɪtərəsi/", "meaning": "The ability to read and write", "example": "Digital literacy is becoming increasingly important in modern education.", "difficulty": "medium"},
                    {"word": "Tutorial", "pronunciation": "/tuˈtɔːriəl/", "meaning": "A period of instruction given by a tutor", "example": "I attended a tutorial session to get help with mathematics.", "difficulty": "medium"},
                    {"word": "Seminar", "pronunciation": "/ˈsɛmɪnɑːr/", "meaning": "A conference or meeting for discussion or training", "example": "The seminar on environmental science was very informative.", "difficulty": "medium"},
                    {"word": "Dissertation", "pronunciation": "/ˌdɪsərˈteɪʃən/", "meaning": "A long essay on a particular subject for a university degree", "example": "She spent two years writing her doctoral dissertation.", "difficulty": "hard"},
                    {"word": "Pedagogy", "pronunciation": "/ˈpɛdəˌɡɑːdʒi/", "meaning": "The method and practice of teaching", "example": "Modern pedagogy emphasizes student-centered learning.", "difficulty": "hard"},
                    {"word": "Graduation", "pronunciation": "/ˌɡrædʒuˈeɪʃən/", "meaning": "The receiving of an academic degree or diploma", "example": "Graduation day was one of the proudest moments of her life.", "difficulty": "easy"},
                    {"word": "Enrollment", "pronunciation": "/ɪnˈroʊlmənt/", "meaning": "The action of registering as a student", "example": "Enrollment for the new semester begins next month.", "difficulty": "medium"},
                    {"word": "Academic", "pronunciation": "/ˌækəˈdɛmɪk/", "meaning": "Relating to education and scholarship", "example": "His academic achievements earned him recognition from the university.", "difficulty": "medium"},
                    {"word": "Intellectual", "pronunciation": "/ˌɪntəˈlɛktʃuəl/", "meaning": "Relating to the intellect or understanding", "example": "The book provides intellectual stimulation for advanced readers.", "difficulty": "hard"},
                    {"word": "Concentration", "pronunciation": "/ˌkɑːnsənˈtreɪʃən/", "meaning": "The ability to focus one's attention", "example": "Good concentration is essential for effective studying.", "difficulty": "medium"}
                ]
            },
            
            "Sports & Recreation": {
                "description": "Sports terminology, recreational activities, and fitness vocabulary",
                "color": "#F97316",
                "vocabulary": [
                    {"word": "Championship", "pronunciation": "/ˈtʃæmpiənʃɪp/", "meaning": "A competition to determine a champion", "example": "The team won the national championship last year.", "difficulty": "medium"},
                    {"word": "Tournament", "pronunciation": "/ˈtʊrnəmənt/", "meaning": "A series of contests between competitors", "example": "The tennis tournament attracts players from around the world.", "difficulty": "medium"},
                    {"word": "Athlete", "pronunciation": "/ˈæθliːt/", "meaning": "A person who competes in sports", "example": "The athlete trained for years to compete in the Olympics.", "difficulty": "easy"},
                    {"word": "Endurance", "pronunciation": "/ɪnˈdʊrəns/", "meaning": "The ability to sustain prolonged physical effort", "example": "Marathon running requires great endurance.", "difficulty": "medium"},
                    {"word": "Agility", "pronunciation": "/əˈdʒɪləti/", "meaning": "The ability to move quickly and easily", "example": "Soccer players need agility to change direction quickly.", "difficulty": "medium"},
                    {"word": "Coordination", "pronunciation": "/koʊˌɔːrdɪˈneɪʃən/", "meaning": "The ability to use different parts of the body together", "example": "Good hand-eye coordination is important in tennis.", "difficulty": "medium"},
                    {"word": "Strategy", "pronunciation": "/ˈstrætədʒi/", "meaning": "A plan of action in sports", "example": "The coach developed a new strategy for the upcoming game.", "difficulty": "medium"},
                    {"word": "Referee", "pronunciation": "/ˌrɛfəˈriː/", "meaning": "An official who supervises a game", "example": "The referee made a controversial call in the final minutes.", "difficulty": "easy"},
                    {"word": "Spectator", "pronunciation": "/ˈspɛkteɪtər/", "meaning": "A person who watches a sporting event", "example": "The stadium was filled with enthusiastic spectators.", "difficulty": "medium"},
                    {"word": "Victory", "pronunciation": "/ˈvɪktəri/", "meaning": "Success in a struggle or contest", "example": "The team celebrated their victory with great joy.", "difficulty": "easy"},
                    {"word": "Defeat", "pronunciation": "/dɪˈfiːt/", "meaning": "The act of losing in a competition", "example": "Despite the defeat, the team played with great spirit.", "difficulty": "easy"},
                    {"word": "Training", "pronunciation": "/ˈtreɪnɪŋ/", "meaning": "The action of teaching skills for a sport", "example": "Daily training is essential for professional athletes.", "difficulty": "easy"},
                    {"word": "Fitness", "pronunciation": "/ˈfɪtnəs/", "meaning": "The condition of being physically fit", "example": "Regular exercise is important for maintaining fitness.", "difficulty": "easy"},
                    {"word": "Competition", "pronunciation": "/ˌkɑːmpəˈtɪʃən/", "meaning": "The activity of competing against others", "example": "The competition was fierce among the top swimmers.", "difficulty": "medium"},
                    {"word": "Performance", "pronunciation": "/pərˈfɔːrməns/", "meaning": "The action of carrying out an activity", "example": "Her performance in the race was outstanding.", "difficulty": "medium"},
                    {"word": "Technique", "pronunciation": "/tɛkˈniːk/", "meaning": "A way of carrying out a particular activity", "example": "Proper technique is crucial for preventing injuries.", "difficulty": "medium"},
                    {"word": "Equipment", "pronunciation": "/ɪˈkwɪpmənt/", "meaning": "The necessary items for a particular purpose", "example": "Safety equipment is required for all participants.", "difficulty": "easy"},
                    {"word": "Recreation", "pronunciation": "/ˌrɛkriˈeɪʃən/", "meaning": "Activity done for enjoyment when not working", "example": "Swimming is a popular form of recreation in summer.", "difficulty": "medium"},
                    {"word": "Leisure", "pronunciation": "/ˈliːʒər/", "meaning": "Free time when one is not working", "example": "He enjoys playing golf in his leisure time.", "difficulty": "medium"},
                    {"word": "Stamina", "pronunciation": "/ˈstæmɪnə/", "meaning": "The ability to sustain prolonged physical effort", "example": "Building stamina requires consistent cardiovascular exercise.", "difficulty": "medium"}
                ]
            },
            
            "Environment & Nature": {
                "description": "Environmental terms, nature vocabulary, and ecological concepts",
                "color": "#22C55E",
                "vocabulary": [
                    {"word": "Ecosystem", "pronunciation": "/ˈiːkoʊˌsɪstəm/", "meaning": "A biological community of interacting organisms", "example": "The rainforest ecosystem is home to thousands of species.", "difficulty": "medium"},
                    {"word": "Biodiversity", "pronunciation": "/ˌbaɪoʊdaɪˈvɜːrsəti/", "meaning": "The variety of life in the world or in a habitat", "example": "Protecting biodiversity is crucial for environmental health.", "difficulty": "hard"},
                    {"word": "Conservation", "pronunciation": "/ˌkɑːnsərˈveɪʃən/", "meaning": "The protection of plants, animals, and natural resources", "example": "Wildlife conservation efforts have helped save endangered species.", "difficulty": "medium"},
                    {"word": "Pollution", "pronunciation": "/pəˈluːʃən/", "meaning": "The presence of harmful substances in the environment", "example": "Air pollution is a major problem in many cities.", "difficulty": "easy"},
                    {"word": "Renewable", "pronunciation": "/rɪˈnuːəbəl/", "meaning": "Able to be replenished naturally", "example": "Solar energy is a renewable source of power.", "difficulty": "medium"},
                    {"word": "Sustainability", "pronunciation": "/səˌsteɪnəˈbɪləti/", "meaning": "The ability to maintain something at a certain rate", "example": "Sustainability is key to protecting our planet for future generations.", "difficulty": "hard"},
                    {"word": "Climate", "pronunciation": "/ˈklaɪmət/", "meaning": "The weather conditions in an area over a long period", "example": "Climate change is affecting weather patterns worldwide.", "difficulty": "easy"},
                    {"word": "Deforestation", "pronunciation": "/diːˌfɔːrɪˈsteɪʃən/", "meaning": "The clearing of forests by cutting down trees", "example": "Deforestation contributes to global warming.", "difficulty": "hard"},
                    {"word": "Habitat", "pronunciation": "/ˈhæbɪtæt/", "meaning": "The natural home of an animal or plant", "example": "Polar bears' habitat is threatened by melting ice.", "difficulty": "medium"},
                    {"word": "Endangered", "pronunciation": "/ɪnˈdeɪndʒərd/", "meaning": "At risk of extinction", "example": "The giant panda is no longer considered endangered.", "difficulty": "medium"},
                    {"word": "Recycling", "pronunciation": "/riˈsaɪklɪŋ/", "meaning": "The process of converting waste into reusable material", "example": "Recycling helps reduce the amount of waste in landfills.", "difficulty": "easy"},
                    {"word": "Greenhouse", "pronunciation": "/ˈɡriːnhaʊs/", "meaning": "A glass building for growing plants; relating to global warming", "example": "Greenhouse gases trap heat in the atmosphere.", "difficulty": "medium"},
                    {"word": "Organic", "pronunciation": "/ɔːrˈɡænɪk/", "meaning": "Produced without artificial chemicals", "example": "Organic farming is better for the environment.", "difficulty": "medium"},
                    {"word": "Fossil", "pronunciation": "/ˈfɑːsəl/", "meaning": "The remains of ancient organisms; relating to fuel", "example": "Fossil fuels are a major source of carbon emissions.", "difficulty": "medium"},
                    {"word": "Wilderness", "pronunciation": "/ˈwɪldərnəs/", "meaning": "An uncultivated, uninhabited region", "example": "The wilderness area is protected from development.", "difficulty": "medium"},
                    {"word": "Erosion", "pronunciation": "/ɪˈroʊʒən/", "meaning": "The gradual destruction of something by natural forces", "example": "Soil erosion is a serious problem for farmers.", "difficulty": "hard"},
                    {"word": "Photosynthesis", "pronunciation": "/ˌfoʊtoʊˈsɪnθəsɪs/", "meaning": "The process by which plants make food using sunlight", "example": "Photosynthesis produces oxygen that we breathe.", "difficulty": "hard"},
                    {"word": "Migration", "pronunciation": "/maɪˈɡreɪʃən/", "meaning": "The movement of animals from one place to another", "example": "Bird migration patterns are changing due to climate change.", "difficulty": "medium"},
                    {"word": "Vegetation", "pronunciation": "/ˌvɛdʒəˈteɪʃən/", "meaning": "Plants considered collectively", "example": "The vegetation in the desert is adapted to dry conditions.", "difficulty": "medium"},
                    {"word": "Atmosphere", "pronunciation": "/ˈætməsˌfɪr/", "meaning": "The layer of gases surrounding the Earth", "example": "The atmosphere protects us from harmful radiation.", "difficulty": "medium"}
                ]
            },
            
            "Arts & Culture": {
                "description": "Vocabulary related to arts, culture, music, and creative expression",
                "color": "#A855F7",
                "vocabulary": [
                    {"word": "Masterpiece", "pronunciation": "/ˈmæstərpiːs/", "meaning": "An outstanding work of art or craft", "example": "The Mona Lisa is considered a masterpiece of Renaissance art.", "difficulty": "medium"},
                    {"word": "Exhibition", "pronunciation": "/ˌɛksəˈbɪʃən/", "meaning": "A public display of works of art", "example": "The museum is hosting an exhibition of modern sculptures.", "difficulty": "medium"},
                    {"word": "Symphony", "pronunciation": "/ˈsɪmfəni/", "meaning": "A long musical composition for orchestra", "example": "Beethoven's Ninth Symphony is one of the most famous classical pieces.", "difficulty": "medium"},
                    {"word": "Sculpture", "pronunciation": "/ˈskʌlptʃər/", "meaning": "The art of making three-dimensional forms", "example": "The sculpture in the park was carved from marble.", "difficulty": "medium"},
                    {"word": "Portrait", "pronunciation": "/ˈpɔːrtrət/", "meaning": "A painting, drawing, or photograph of a person", "example": "The artist painted a beautiful portrait of the queen.", "difficulty": "easy"},
                    {"word": "Gallery", "pronunciation": "/ˈɡæləri/", "meaning": "A room or building for displaying art", "example": "We spent the afternoon visiting art galleries downtown.", "difficulty": "easy"},
                    {"word": "Performance", "pronunciation": "/pərˈfɔːrməns/", "meaning": "An act of presenting a play, concert, or other entertainment", "example": "The dance performance was absolutely stunning.", "difficulty": "medium"},
                    {"word": "Creativity", "pronunciation": "/ˌkriːeɪˈtɪvəti/", "meaning": "The use of imagination to create something new", "example": "Creativity is essential for artistic expression.", "difficulty": "medium"},
                    {"word": "Inspiration", "pronunciation": "/ˌɪnspəˈreɪʃən/", "meaning": "The process of being mentally stimulated to create", "example": "The artist found inspiration in the beauty of nature.", "difficulty": "medium"},
                    {"word": "Tradition", "pronunciation": "/trəˈdɪʃən/", "meaning": "The transmission of customs or beliefs", "example": "The festival celebrates our cultural traditions.", "difficulty": "easy"},
                    {"word": "Heritage", "pronunciation": "/ˈhɛrətɪdʒ/", "meaning": "Property that is inherited; cultural legacy", "example": "The old building is part of our architectural heritage.", "difficulty": "medium"},
                    {"word": "Aesthetic", "pronunciation": "/ɛsˈθɛtɪk/", "meaning": "Concerned with beauty or artistic taste", "example": "The room has a modern aesthetic with clean lines.", "difficulty": "hard"},
                    {"word": "Composition", "pronunciation": "/ˌkɑːmpəˈzɪʃən/", "meaning": "The arrangement of elements in a work of art", "example": "The composition of the painting draws the eye to the center.", "difficulty": "medium"},
                    {"word": "Melody", "pronunciation": "/ˈmɛlədi/", "meaning": "A sequence of musical notes that form the main tune", "example": "The melody of that song is very catchy.", "difficulty": "easy"},
                    {"word": "Rhythm", "pronunciation": "/ˈrɪðəm/", "meaning": "A strong, regular pattern of movement or sound", "example": "The dancers moved in perfect rhythm with the music.", "difficulty": "easy"},
                    {"word": "Literature", "pronunciation": "/ˈlɪtərətʃər/", "meaning": "Written works, especially those considered of superior quality", "example": "She studied English literature at university.", "difficulty": "medium"},
                    {"word": "Poetry", "pronunciation": "/ˈpoʊətri/", "meaning": "Literary work in which expression of feelings is given intensity", "example": "His poetry captures the beauty of everyday moments.", "difficulty": "easy"},
                    {"word": "Drama", "pronunciation": "/ˈdrɑːmə/", "meaning": "A play for theater, radio, or television", "example": "The drama tells the story of a family during wartime.", "difficulty": "easy"},
                    {"word": "Architecture", "pronunciation": "/ˈɑːrkɪtɛktʃər/", "meaning": "The design and construction of buildings", "example": "The architecture of the cathedral is breathtaking.", "difficulty": "medium"},
                    {"word": "Renaissance", "pronunciation": "/ˈrɛnəsɑːns/", "meaning": "A period of renewed interest in art and learning", "example": "The Renaissance was a time of great artistic achievement.", "difficulty": "hard"}
                ]
            },
            
            "Science & Research": {
                "description": "Scientific terminology, research methods, and laboratory vocabulary",
                "color": "#0EA5E9",
                "vocabulary": [
                    {"word": "Hypothesis", "pronunciation": "/haɪˈpɑːθəsɪs/", "meaning": "A proposed explanation for a phenomenon", "example": "The scientist tested her hypothesis through careful experiments.", "difficulty": "hard"},
                    {"word": "Experiment", "pronunciation": "/ɪkˈspɛrəmənt/", "meaning": "A scientific procedure to test a hypothesis", "example": "The experiment proved that the theory was correct.", "difficulty": "medium"},
                    {"word": "Laboratory", "pronunciation": "/ˈlæbrəˌtɔːri/", "meaning": "A room equipped for scientific experiments", "example": "The students conducted their research in the chemistry laboratory.", "difficulty": "medium"},
                    {"word": "Molecule", "pronunciation": "/ˈmɑːlɪkjuːl/", "meaning": "A group of atoms bonded together", "example": "Water is a molecule made of hydrogen and oxygen atoms.", "difficulty": "medium"},
                    {"word": "Microscope", "pronunciation": "/ˈmaɪkrəskoʊp/", "meaning": "An instrument for viewing very small objects", "example": "We used a microscope to examine the bacteria.", "difficulty": "medium"},
                    {"word": "Discovery", "pronunciation": "/dɪˈskʌvəri/", "meaning": "The action of finding something new", "example": "The discovery of penicillin revolutionized medicine.", "difficulty": "medium"},
                    {"word": "Theory", "pronunciation": "/ˈθɪri/", "meaning": "A well-substantiated explanation of natural phenomena", "example": "Einstein's theory of relativity changed our understanding of physics.", "difficulty": "medium"},
                    {"word": "Evidence", "pronunciation": "/ˈɛvədəns/", "meaning": "Information supporting a conclusion", "example": "The evidence strongly supports the scientist's conclusion.", "difficulty": "easy"},
                    {"word": "Analysis", "pronunciation": "/əˈnæləsɪs/", "meaning": "Detailed examination of elements or structure", "example": "The analysis of the data revealed surprising patterns.", "difficulty": "medium"},
                    {"word": "Research", "pronunciation": "/rɪˈsɜːrtʃ/", "meaning": "Systematic investigation to establish facts", "example": "Medical research has led to many life-saving treatments.", "difficulty": "medium"},
                    {"word": "Observation", "pronunciation": "/ˌɑːbzərˈveɪʃən/", "meaning": "The action of watching something carefully", "example": "Careful observation is the first step in scientific inquiry.", "difficulty": "medium"},
                    {"word": "Conclusion", "pronunciation": "/kənˈkluːʒən/", "meaning": "A judgment reached by reasoning", "example": "The conclusion of the study was published in a scientific journal.", "difficulty": "easy"},
                    {"word": "Variable", "pronunciation": "/ˈvɛriəbəl/", "meaning": "An element that can change in an experiment", "example": "Temperature was the only variable in the experiment.", "difficulty": "hard"},
                    {"word": "Formula", "pronunciation": "/ˈfɔːrmjələ/", "meaning": "A mathematical relationship or rule", "example": "The formula for calculating speed is distance divided by time.", "difficulty": "medium"},
                    {"word": "Genetics", "pronunciation": "/dʒəˈnɛtɪks/", "meaning": "The study of heredity and genes", "example": "Genetics helps us understand how traits are passed to offspring.", "difficulty": "hard"},
                    {"word": "Evolution", "pronunciation": "/ˌɛvəˈluːʃən/", "meaning": "The gradual development of species over time", "example": "Evolution explains the diversity of life on Earth.", "difficulty": "medium"},
                    {"word": "Organism", "pronunciation": "/ˈɔːrɡəˌnɪzəm/", "meaning": "An individual living thing", "example": "Bacteria are single-celled organisms.", "difficulty": "medium"},
                    {"word": "Specimen", "pronunciation": "/ˈspɛsəmən/", "meaning": "A sample taken for scientific study", "example": "The museum has a specimen of every local bird species.", "difficulty": "medium"},
                    {"word": "Innovation", "pronunciation": "/ˌɪnəˈveɪʃən/", "meaning": "The introduction of new ideas or methods", "example": "Scientific innovation drives technological progress.", "difficulty": "medium"},
                    {"word": "Phenomenon", "pronunciation": "/fəˈnɑːmənən/", "meaning": "A fact or situation that can be observed", "example": "The aurora borealis is a beautiful natural phenomenon.", "difficulty": "hard"}
                ]
            },
            
            "Home & Family": {
                "description": "Vocabulary related to home life, family relationships, and household items",
                "color": "#F472B6",
                "vocabulary": [
                    {"word": "Household", "pronunciation": "/ˈhaʊshoʊld/", "meaning": "A house and its occupants regarded as a unit", "example": "Our household consists of four family members.", "difficulty": "medium"},
                    {"word": "Furniture", "pronunciation": "/ˈfɜːrnɪtʃər/", "meaning": "Movable articles that make a room suitable for living", "example": "We bought new furniture for the living room.", "difficulty": "easy"},
                    {"word": "Appliance", "pronunciation": "/əˈplaɪəns/", "meaning": "A device designed to perform a specific task", "example": "The washing machine is an essential household appliance.", "difficulty": "medium"},
                    {"word": "Relative", "pronunciation": "/ˈrɛlətɪv/", "meaning": "A person connected by blood or marriage", "example": "All my relatives gathered for the family reunion.", "difficulty": "easy"},
                    {"word": "Generation", "pronunciation": "/ˌdʒɛnəˈreɪʃən/", "meaning": "All people born around the same time", "example": "Three generations of our family live in this house.", "difficulty": "medium"},
                    {"word": "Sibling", "pronunciation": "/ˈsɪblɪŋ/", "meaning": "A brother or sister", "example": "I have two siblings: an older brother and a younger sister.", "difficulty": "medium"},
                    {"word": "Ancestor", "pronunciation": "/ˈænsɛstər/", "meaning": "A person from whom one is descended", "example": "My ancestors came to this country over a century ago.", "difficulty": "medium"},
                    {"word": "Descendant", "pronunciation": "/dɪˈsɛndənt/", "meaning": "A person who is descended from a particular ancestor", "example": "She is a descendant of the town's founder.", "difficulty": "hard"},
                    {"word": "Inheritance", "pronunciation": "/ɪnˈhɛrətəns/", "meaning": "Property received from an ancestor", "example": "The house was part of his inheritance from his grandmother.", "difficulty": "hard"},
                    {"word": "Chore", "pronunciation": "/tʃɔːr/", "meaning": "A routine task, especially household work", "example": "Washing dishes is my least favorite chore.", "difficulty": "easy"},
                    {"word": "Maintenance", "pronunciation": "/ˈmeɪntənəns/", "meaning": "The process of keeping something in good condition", "example": "Regular maintenance keeps the house in good repair.", "difficulty": "medium"},
                    {"word": "Decoration", "pronunciation": "/ˌdɛkəˈreɪʃən/", "meaning": "The process of making something look attractive", "example": "We put up decorations for the holiday celebration.", "difficulty": "medium"},
                    {"word": "Privacy", "pronunciation": "/ˈpraɪvəsi/", "meaning": "The state of being free from public attention", "example": "Everyone in the family needs some privacy.", "difficulty": "medium"},
                    {"word": "Comfort", "pronunciation": "/ˈkʌmfərt/", "meaning": "A state of physical ease and freedom from pain", "example": "The soft sofa provides great comfort for reading.", "difficulty": "easy"},
                    {"word": "Security", "pronunciation": "/sɪˈkjʊrəti/", "meaning": "The state of being protected from danger", "example": "We installed a security system to protect our home.", "difficulty": "medium"},
                    {"word": "Hospitality", "pronunciation": "/ˌhɑːspɪˈtæləti/", "meaning": "The friendly reception and treatment of guests", "example": "Their hospitality made us feel welcome in their home.", "difficulty": "hard"},
                    {"word": "Tradition", "pronunciation": "/trəˈdɪʃən/", "meaning": "The transmission of customs within a family", "example": "It's a family tradition to have dinner together every Sunday.", "difficulty": "easy"},
                    {"word": "Responsibility", "pronunciation": "/rɪˌspɑːnsəˈbɪləti/", "meaning": "The state of having a duty to deal with something", "example": "Taking care of pets is a big responsibility for children.", "difficulty": "medium"},
                    {"word": "Harmony", "pronunciation": "/ˈhɑːrməni/", "meaning": "A state of peaceful coexistence", "example": "The family lives in harmony despite their differences.", "difficulty": "medium"},
                    {"word": "Nurture", "pronunciation": "/ˈnɜːrtʃər/", "meaning": "To care for and encourage growth", "example": "Parents nurture their children with love and guidance.", "difficulty": "medium"}
                ]
            },
            
            "Weather & Climate": {
                "description": "Weather phenomena, climate patterns, and meteorological terms",
                "color": "#06B6D4",
                "vocabulary": [
                    {"word": "Temperature", "pronunciation": "/ˈtɛmpərətʃər/", "meaning": "The degree of hotness or coldness", "example": "The temperature dropped below freezing last night.", "difficulty": "easy"},
                    {"word": "Humidity", "pronunciation": "/hjuˈmɪdəti/", "meaning": "The amount of water vapor in the air", "example": "High humidity makes the weather feel much hotter.", "difficulty": "medium"},
                    {"word": "Precipitation", "pronunciation": "/prɪˌsɪpəˈteɪʃən/", "meaning": "Rain, snow, sleet, or hail", "example": "The weather forecast predicts heavy precipitation this weekend.", "difficulty": "hard"},
                    {"word": "Atmosphere", "pronunciation": "/ˈætməsˌfɪr/", "meaning": "The layer of gases surrounding Earth", "example": "The atmosphere protects us from harmful solar radiation.", "difficulty": "medium"},
                    {"word": "Barometer", "pronunciation": "/bəˈrɑːmətər/", "meaning": "An instrument measuring atmospheric pressure", "example": "The barometer indicates that a storm is approaching.", "difficulty": "hard"},
                    {"word": "Forecast", "pronunciation": "/ˈfɔːrkæst/", "meaning": "A prediction of future weather conditions", "example": "The weather forecast calls for sunny skies tomorrow.", "difficulty": "medium"},
                    {"word": "Hurricane", "pronunciation": "/ˈhɜːrəkən/", "meaning": "A severe tropical storm with high winds", "example": "The hurricane caused widespread damage along the coast.", "difficulty": "medium"},
                    {"word": "Tornado", "pronunciation": "/tɔːrˈneɪdoʊ/", "meaning": "A violently rotating column of air", "example": "The tornado destroyed several buildings in its path.", "difficulty": "medium"},
                    {"word": "Blizzard", "pronunciation": "/ˈblɪzərd/", "meaning": "A severe snowstorm with high winds", "example": "The blizzard made travel impossible for two days.", "difficulty": "medium"},
                    {"word": "Drought", "pronunciation": "/draʊt/", "meaning": "A prolonged period of abnormally low rainfall", "example": "The drought has lasted for three months without rain.", "difficulty": "medium"},
                    {"word": "Monsoon", "pronunciation": "/mɑːnˈsuːn/", "meaning": "A seasonal wind bringing heavy rains", "example": "The monsoon season provides most of the year's rainfall.", "difficulty": "hard"},
                    {"word": "Frost", "pronunciation": "/frɔːst/", "meaning": "Ice crystals formed when water vapor freezes", "example": "Frost covered the grass early this morning.", "difficulty": "easy"},
                    {"word": "Hail", "pronunciation": "/heɪl/", "meaning": "Pellets of frozen rain", "example": "The hail was so large it damaged car windshields.", "difficulty": "easy"},
                    {"word": "Lightning", "pronunciation": "/ˈlaɪtnɪŋ/", "meaning": "A bright flash of electricity in the sky", "example": "Lightning lit up the dark storm clouds.", "difficulty": "easy"},
                    {"word": "Thunder", "pronunciation": "/ˈθʌndər/", "meaning": "The sound that follows lightning", "example": "The thunder was so loud it shook the windows.", "difficulty": "easy"},
                    {"word": "Breeze", "pronunciation": "/briːz/", "meaning": "A gentle wind", "example": "A cool breeze made the hot day more comfortable.", "difficulty": "easy"},
                    {"word": "Gale", "pronunciation": "/ɡeɪl/", "meaning": "A very strong wind", "example": "The gale force winds knocked down several trees.", "difficulty": "medium"},
                    {"word": "Overcast", "pronunciation": "/ˈoʊvərkæst/", "meaning": "Covered with clouds; cloudy", "example": "The sky has been overcast all day.", "difficulty": "medium"},
                    {"word": "Visibility", "pronunciation": "/ˌvɪzəˈbɪləti/", "meaning": "The distance one can see clearly", "example": "Fog reduced visibility to less than 100 meters.", "difficulty": "medium"},
                    {"word": "Seasonal", "pronunciation": "/ˈsiːzənəl/", "meaning": "Relating to or characteristic of a season", "example": "Seasonal changes affect plant growth patterns.", "difficulty": "medium"}
                ]
            },
            
            "Emotions & Feelings": {
                "description": "Vocabulary for expressing emotions, feelings, and psychological states",
                "color": "#EC4899",
                "vocabulary": [
                    {"word": "Happiness", "pronunciation": "/ˈhæpɪnəs/", "meaning": "The feeling of joy and contentment", "example": "Her happiness was evident in her bright smile.", "difficulty": "easy"},
                    {"word": "Sadness", "pronunciation": "/ˈsædnəs/", "meaning": "The feeling of sorrow or unhappiness", "example": "The movie's ending filled me with sadness.", "difficulty": "easy"},
                    {"word": "Anxiety", "pronunciation": "/æŋˈzaɪəti/", "meaning": "A feeling of worry or nervousness", "example": "She felt anxiety before her job interview.", "difficulty": "medium"},
                    {"word": "Excitement", "pronunciation": "/ɪkˈsaɪtmənt/", "meaning": "A feeling of great enthusiasm and eagerness", "example": "The children's excitement about the trip was contagious.", "difficulty": "medium"},
                    {"word": "Frustration", "pronunciation": "/frʌˈstreɪʃən/", "meaning": "The feeling of being upset due to inability to achieve something", "example": "His frustration grew when the computer kept crashing.", "difficulty": "medium"},
                    {"word": "Contentment", "pronunciation": "/kənˈtɛntmənt/", "meaning": "A state of peaceful happiness and satisfaction", "example": "She found contentment in her simple life.", "difficulty": "medium"},
                    {"word": "Disappointment", "pronunciation": "/ˌdɪsəˈpɔɪntmənt/", "meaning": "Sadness from unfulfilled expectations", "example": "The cancellation of the concert was a great disappointment.", "difficulty": "medium"},
                    {"word": "Enthusiasm", "pronunciation": "/ɪnˈθuːziæzəm/", "meaning": "Intense and eager enjoyment or interest", "example": "Her enthusiasm for learning new languages is inspiring.", "difficulty": "medium"},
                    {"word": "Melancholy", "pronunciation": "/ˈmɛlənkɑːli/", "meaning": "A pensive sadness or thoughtful sorrow", "example": "The autumn rain filled him with melancholy.", "difficulty": "hard"},
                    {"word": "Euphoria", "pronunciation": "/juˈfɔːriə/", "meaning": "A feeling of intense excitement and happiness", "example": "Winning the championship filled the team with euphoria.", "difficulty": "hard"},
                    {"word": "Empathy", "pronunciation": "/ˈɛmpəθi/", "meaning": "The ability to understand others' feelings", "example": "Her empathy made her an excellent counselor.", "difficulty": "medium"},
                    {"word": "Compassion", "pronunciation": "/kəmˈpæʃən/", "meaning": "Sympathetic concern for others' suffering", "example": "The nurse showed great compassion for her patients.", "difficulty": "medium"},
                    {"word": "Gratitude", "pronunciation": "/ˈɡrætɪtuːd/", "meaning": "The quality of being thankful", "example": "She expressed gratitude for all the help she received.", "difficulty": "medium"},
                    {"word": "Resentment", "pronunciation": "/rɪˈzɛntmənt/", "meaning": "Bitter indignation at unfair treatment", "example": "He harbored resentment about being passed over for promotion.", "difficulty": "hard"},
                    {"word": "Serenity", "pronunciation": "/səˈrɛnəti/", "meaning": "The state of being calm and peaceful", "example": "The meditation brought her a sense of serenity.", "difficulty": "hard"},
                    {"word": "Nostalgia", "pronunciation": "/nɑːˈstældʒə/", "meaning": "Sentimental longing for the past", "example": "Looking at old photos filled him with nostalgia.", "difficulty": "hard"},
                    {"word": "Optimism", "pronunciation": "/ˈɑːptɪmɪzəm/", "meaning": "Hopefulness about the future", "example": "Her optimism helped the team through difficult times.", "difficulty": "medium"},
                    {"word": "Pessimism", "pronunciation": "/ˈpɛsəmɪzəm/", "meaning": "A tendency to see the worst in situations", "example": "His pessimism made it hard for others to stay motivated.", "difficulty": "medium"},
                    {"word": "Confidence", "pronunciation": "/ˈkɑːnfɪdəns/", "meaning": "The feeling of self-assurance", "example": "Practice helped build her confidence in public speaking.", "difficulty": "easy"},
                    {"word": "Vulnerability", "pronunciation": "/ˌvʌlnərəˈbɪləti/", "meaning": "The quality of being emotionally exposed", "example": "Sharing personal stories requires vulnerability and courage.", "difficulty": "hard"}
                ]
            },
            
            "Communication & Language": {
                "description": "Terms related to communication, language learning, and linguistic concepts",
                "color": "#8B5CF6",
                "vocabulary": [
                    {"word": "Vocabulary", "pronunciation": "/voʊˈkæbjəˌlɛri/", "meaning": "The body of words used in a particular language", "example": "Reading books helps expand your vocabulary.", "difficulty": "medium"},
                    {"word": "Grammar", "pronunciation": "/ˈɡræmər/", "meaning": "The rules for using words in a language", "example": "Good grammar is important for clear communication.", "difficulty": "easy"},
                    {"word": "Pronunciation", "pronunciation": "/prəˌnʌnsiˈeɪʃən/", "meaning": "The way words are spoken", "example": "Her pronunciation of English words has improved greatly.", "difficulty": "medium"},
                    {"word": "Fluency", "pronunciation": "/ˈfluːənsi/", "meaning": "The ability to speak smoothly and easily", "example": "Achieving fluency in a foreign language takes practice.", "difficulty": "medium"},
                    {"word": "Accent", "pronunciation": "/ˈæksɛnt/", "meaning": "A distinctive way of pronouncing words", "example": "She speaks English with a slight French accent.", "difficulty": "easy"},
                    {"word": "Dialect", "pronunciation": "/ˈdaɪəlɛkt/", "meaning": "A regional variety of a language", "example": "The southern dialect has unique expressions and pronunciations.", "difficulty": "medium"},
                    {"word": "Translation", "pronunciation": "/trænsˈleɪʃən/", "meaning": "Converting text from one language to another", "example": "The translation of the novel took six months to complete.", "difficulty": "medium"},
                    {"word": "Interpretation", "pronunciation": "/ɪnˌtɜːrprəˈteɪʃən/", "meaning": "Oral translation between languages", "example": "The conference provided interpretation in five languages.", "difficulty": "hard"},
                    {"word": "Bilingual", "pronunciation": "/baɪˈlɪŋɡwəl/", "meaning": "Able to speak two languages fluently", "example": "Being bilingual is an advantage in today's global economy.", "difficulty": "medium"},
                    {"word": "Multilingual", "pronunciation": "/ˌmʌltiˈlɪŋɡwəl/", "meaning": "Able to speak several languages", "example": "The multilingual staff can assist customers from many countries.", "difficulty": "hard"},
                    {"word": "Conversation", "pronunciation": "/ˌkɑːnvərˈseɪʃən/", "meaning": "An informal talk between people", "example": "We had an interesting conversation about travel experiences.", "difficulty": "easy"},
                    {"word": "Discussion", "pronunciation": "/dɪˈskʌʃən/", "meaning": "A detailed conversation about a topic", "example": "The discussion about climate change lasted for hours.", "difficulty": "easy"},
                    {"word": "Debate", "pronunciation": "/dɪˈbeɪt/", "meaning": "A formal argument about opposing views", "example": "The presidential debate will be broadcast live tonight.", "difficulty": "medium"},
                    {"word": "Presentation", "pronunciation": "/ˌpriːzənˈteɪʃən/", "meaning": "A formal talk to an audience", "example": "Her presentation on renewable energy was very informative.", "difficulty": "medium"},
                    {"word": "Articulation", "pronunciation": "/ɑːrˌtɪkjəˈleɪʃən/", "meaning": "Clear and effective expression of ideas", "example": "Good articulation is essential for public speakers.", "difficulty": "hard"},
                    {"word": "Eloquence", "pronunciation": "/ˈɛləkwəns/", "meaning": "Fluent and persuasive speaking", "example": "The politician's eloquence won over many voters.", "difficulty": "hard"},
                    {"word": "Comprehension", "pronunciation": "/ˌkɑːmprɪˈhɛnʃən/", "meaning": "The ability to understand language", "example": "Reading comprehension improves with regular practice.", "difficulty": "medium"},
                    {"word": "Expression", "pronunciation": "/ɪkˈsprɛʃən/", "meaning": "The conveying of thoughts or feelings", "example": "Art is a form of creative expression.", "difficulty": "easy"},
                    {"word": "Gesture", "pronunciation": "/ˈdʒɛstʃər/", "meaning": "A movement of the body to express meaning", "example": "Hand gestures can help emphasize your points when speaking.", "difficulty": "easy"},
                    {"word": "Intonation", "pronunciation": "/ˌɪntəˈneɪʃən/", "meaning": "The rise and fall of voice in speaking", "example": "Proper intonation can change the meaning of a sentence.", "difficulty": "hard"}
                ]
            }
        }

        # Create topics and vocabulary
        for topic_name, topic_info in topics_data.items():
            self.stdout.write(f'Creating topic: {topic_name}')
            
            topic = Topic.objects.create(
                name=topic_name,
                description=topic_info["description"],
                color=topic_info["color"]
            )
            
            # Create vocabulary for this topic
            for vocab_data in topic_info["vocabulary"]:
                Vocabulary.objects.create(
                    topic=topic,
                    word=vocab_data["word"],
                    pronunciation=vocab_data["pronunciation"],
                    meaning=vocab_data["meaning"],
                    example=vocab_data["example"],
                    difficulty=vocab_data["difficulty"]
                )
            
            self.stdout.write(f'Created {len(topic_info["vocabulary"])} vocabulary items for {topic_name}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully loaded {Topic.objects.count()} topics and {Vocabulary.objects.count()} vocabulary items'
            )
        )