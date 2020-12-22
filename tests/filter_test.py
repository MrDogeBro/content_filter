import unittest

from content_filter import Filter


class TestFilter(unittest.TestCase):
    def accuracy_test(self):
        filter = Filter()

        self.assertEqual(filter.check("FUCK YOU BITCH").as_bool, True)
        self.assertEqual(filter.check(
            "Hi there, how are you doing today?").as_bool, False)
        self.assertEqual(filter.check("Im good, hbu?").as_bool, False)
        self.assertEqual(filter.check(
            "I'm good, how about you?").as_bool, False)
        self.assertEqual(filter.check(
            "The small white buoys marked the location of hundreds of crab pots.").as_bool, False)
        self.assertEqual(filter.check("what da fuck").as_bool, True)
        self.assertEqual(filter.check("eat my ass").as_bool, True)
        self.assertEqual(filter.check(
            "The ants enjoyed the barbecue more than the family.").as_bool, False)
        self.assertEqual(filter.check(
            "Car safety systems have come a long way, but he was out to prove they could be outsmarted.").as_bool, False)
        self.assertEqual(filter.check(
            "At that moment he wasn't listening to music, he was living an experience.").as_bool, False)
        self.assertEqual(filter.check(
            "He invested some skill points in Charisma and Strength.").as_bool, False)
        self.assertEqual(filter.check(
            "He wore the surgical mask in public not to keep from catching a virus, but to keep people away from him.").as_bool, False)
        self.assertEqual(filter.check(
            "Peanut butter and jelly caused the elderly lady to think about her past.").as_bool, False)
        self.assertEqual(filter.check(
            "He found the chocolate covered roaches quite tasty.").as_bool, False)
        self.assertEqual(filter.check(
            "I currently have 4 windows open up… and I don’t know why.").as_bool, False)
        self.assertEqual(filter.check(
            "The efficiency we have at removing trash has made creating trash more acceptable.").as_bool, False)
        self.assertEqual(filter.check(
            "Chocolate covered crickets were his favorite snack.").as_bool, False)
        self.assertEqual(filter.check(
            "He stepped gingerly onto the bridge knowing that enchantment awaited on the other side.").as_bool, False)
        self.assertEqual(filter.check(
            "25 years later, she still regretted that specific moment.").as_bool, False)
        self.assertEqual(filter.check(
            "They wandered into a strange Tiki bar on the edge of the small beach town.").as_bool, False)
        self.assertEqual(filter.check(
            "I like to suck d***").as_bool, True)
        self.assertEqual(filter.check(
            "what os this $h!+").as_bool, True)
        self.assertEqual(filter.check(
            "I'm confused: when people ask me what's up, and I point, they groan.").as_bool, False)
        self.assertEqual(filter.check(
            "It's difficult to understand the lengths he'd go to remain short.").as_bool, False)
        self.assertEqual(filter.check(
            "Each person who knows you has a different perception of who you are.").as_bool, False)
        self.assertEqual(filter.check(
            "It would have been a better night if the guys next to us weren't in the splash zone.").as_bool, False)
        self.assertEqual(filter.check(
            "His thought process was on so many levels that he gave himself a phobia of heights.").as_bool, False)
        self.assertEqual(filter.check(
            "While on the first date he accidentally hit his head on the beam.").as_bool, False)
        self.assertEqual(filter.check(
            "He decided that the time had come to be stronger than any of the excuses he'd used until then.").as_bool, False)
        self.assertEqual(filter.check("got any d!ld0s?").as_bool, True)
        self.assertEqual(filter.check(
            "When I was little I had a car door slammed shut on my hand and I still remember it quite vividly.").as_bool, False)
        self.assertEqual(filter.check(
            "I checked to make sure that he was still alive.").as_bool, False)
        self.assertEqual(filter.check(
            "The beauty of the sunset was obscured by the industrial cranes.").as_bool, False)
        self.assertEqual(filter.check(
            "The near-death experience brought new ideas to light.").as_bool, False)
        self.assertEqual(filter.check(
            "The truth is that you pay for your lifestyle in hours.").as_bool, False)
        self.assertEqual(filter.check(
            "The view from the lighthouse excited even the most seasoned traveler.").as_bool, False)
        self.assertEqual(filter.check(
            "He found the end of the rainbow and was surprised at what he found there.").as_bool, False)
        self.assertEqual(filter.check(
            "She finally understood that grief was her love with no place for it to go.").as_bool, False)
        self.assertEqual(filter.check(
            "u got a nice pu$$y girl?").as_bool, True)
        self.assertEqual(filter.check(
            "go to he!l you idiot").as_bool, True)
        self.assertEqual(filter.check(
            "There aren't enough towels in the world to stop the sewage flowing from his mouth.").as_bool, False)
        self.assertEqual(filter.check(
            "Swim at your own risk was taken as a challenge for the group of Kansas City college students.").as_bool, False)
        self.assertEqual(filter.check(
            "She had a habit of taking showers in lemonade.").as_bool, False)
        self.assertEqual(filter.check(
            "He was 100% into fasting with her until he understood that meant he couldn't eat.").as_bool, False)
        self.assertEqual(filter.check(
            "On a scale from one to ten, what's your favorite flavor of random grammar?").as_bool, False)
        self.assertEqual(filter.check(
            "25 years later, she still regretted that specific moment.").as_bool, False)
        self.assertEqual(filter.check(
            "He waited for the stop sign to turn to a go sign.").as_bool, False)
        self.assertEqual(filter.check(
            "oh girl giv me dem t1+s").as_bool, True)
        self.assertEqual(filter.check(
            "How about you shows me your b00b$ tonight?").as_bool, True)
        self.assertEqual(filter.check(
            "Lets have $3x tonight baby girl?").as_bool, True)
        self.assertEqual(filter.check(
            "Im gonna rap3 you little girl").as_bool, True)
        self.assertEqual(filter.check(
            "He had concluded that pigs must be able to fly in Hog Heaven.").as_bool, False)
        self.assertEqual(filter.check(
            "We have a lot of rain in June.").as_bool, False)
        self.assertEqual(filter.check(
            "He quietly entered the museum as the super bowl started.").as_bool, False)
        self.assertEqual(filter.check(
            "I am happy to take your donation; any amount will be greatly appreciated.").as_bool, False)
        self.assertEqual(filter.check(
            "Potato wedges probably are not best for relationships.").as_bool, False)
        self.assertEqual(filter.check(
            "You're unsure whether or not to trust him, but very thankful that you wore a turtle neck.").as_bool, False)
        self.assertEqual(filter.check(
            "He picked up trash in his spare time to dump in his neighbor's yard.").as_bool, False)
        self.assertEqual(filter.check(
            "At that moment she realized she had a sixth sense.").as_bool, False)
        self.assertEqual(filter.check(
            "You would be a great p0rn star girl!").as_bool, True)
        self.assertEqual(filter.check(
            "Charles ate the french fries knowing they would be his last meal.").as_bool, False)
        self.assertEqual(filter.check(
            "Let me insert myself into that vjayjay girl").as_bool, True)
        self.assertEqual(filter.check(
            "Don't be scared to drop dem panties girl").as_bool, True)
        self.assertEqual(filter.check(
            "Make sure to lube up your vaj before we get down").as_bool, True)
        self.assertEqual(filter.check(
            "The opportunity of a lifetime passed before him as he tried to decide between a cone or a cup.").as_bool, False)
        self.assertEqual(filter.check(
            "She tilted her head back and let whip cream stream into her mouth while taking a bath.").as_bool, False)
        self.assertEqual(filter.check(
            "They throw cabbage that turns your brain into emotional baggage.").as_bool, False)
        self.assertEqual(filter.check(
            "The newly planted trees were held up by wooden frames in hopes they could survive the next storm.").as_bool, False)
        self.assertEqual(filter.check(
            "She says she has the ability to hear the soundtrack of your life.").as_bool, False)
        self.assertEqual(filter.check(
            "We have young kids who often walk into our room at night for various reasons including clowns in the closet.").as_bool, False)
        self.assertEqual(filter.check(
            "It's much more difficult to play tennis with a bowling ball than it is to bowl with a tennis ball.").as_bool, False)
        self.assertEqual(filter.check(
            "Most shark attacks occur about 10 feet from the beach since that's where the people are.").as_bool, False)
        self.assertEqual(filter.check(
            "Of course, she loves her pink bunny slippers.").as_bool, False)
        self.assertEqual(filter.check(
            "It didn't make sense unless you had the power to eat colors.").as_bool, False)
        self.assertEqual(filter.check(
            "After exploring the abandoned building, he started to believe in ghosts.").as_bool, False)
        self.assertEqual(filter.check(
            "He learned the important lesson that a picnic at the beach on a windy day is a bad idea.").as_bool, False)
        self.assertEqual(filter.check(
            "The shark-infested South Pine channel was the only way in or out.").as_bool, False)
        self.assertEqual(filter.check(
            "The skeleton had skeletons of his own in the closet.").as_bool, False)
        self.assertEqual(filter.check(
            "He was willing to find the depths of the rabbit hole in order to be with her.").as_bool, False)
        self.assertEqual(filter.check("you wh0@r!").as_bool, True)
        self.assertEqual(filter.check(
            "He didn’t want to go to the dentist, yet he went anyway.").as_bool, False)
        self.assertEqual(filter.check(
            "Girl, r u a h0ok3r?").as_bool, True)
        self.assertEqual(filter.check(
            "lets get naked up in here").as_bool, True)
        self.assertEqual(filter.check(
            "Check back tomorrow; I will see if the book has arrived.").as_bool, False)
        self.assertEqual(filter.check(
            "I would be delighted if the sea were full of cucumber juice.").as_bool, False)
        self.assertEqual(filter.check(
            "Even though he thought the world was flat he didn’t see the irony of wanting to travel around the world.").as_bool, False)
        self.assertEqual(filter.check(
            "Lets all be unique together until we realise we are all the same.").as_bool, False)
        self.assertEqual(filter.check(
            "Hit me with your pet shark!").as_bool, False)
        self.assertEqual(filter.check(
            "I met an interesting turtle while the song on the radio blasted away.").as_bool, False)
        self.assertEqual(filter.check(
            "You always look best when your nude!").as_bool, True)
        self.assertEqual(filter.check(
            "Be careful with that butter knife.").as_bool, False)
        self.assertEqual(filter.check(
            "I am my aunt's sister's daughter.").as_bool, False)
        self.assertEqual(filter.check(
            "Toddlers feeding raccoons surprised even the seasoned park ranger.").as_bool, False)
        self.assertEqual(filter.check(
            "FFFFFFFFFFUUUUUUUUUUUUUUUUUUUUUUCCCCCCCCCCKKKKKKKKKKK ME!!!!!").as_bool, True)
        self.assertEqual(filter.check(
            "She wondered what his eyes were saying beneath his mirrored sunglasses.").as_bool, False)
        self.assertEqual(filter.check(
            "The lyrics of the song sounded like fingernails on a chalkboard.").as_bool, False)
        self.assertEqual(filter.check(
            "Nothing seemed out of place except the washing machine in the bar.").as_bool, False)
        self.assertEqual(filter.check(
            "When transplanting seedlings, candied teapots will make the task easier.").as_bool, False)
        self.assertEqual(filter.check(
            "He learned the hardest lesson of his life and had the scars, both physical and mental, to prove it.").as_bool, False)
        self.assertEqual(filter.check(
            "You bite up because of your lower jaw.").as_bool, False)
        self.assertEqual(filter.check(
            "The mysterious diary records the voice.").as_bool, False)
        self.assertEqual(filter.check(
            "Hello there, how are you doing today?").as_bool, False)
        self.assertEqual(filter.check("scunthorpe").as_bool, False)

    def filter_list_test(self):
        filter = Filter()

        self.assertEqual(filter.check("You always look best when your nude!").as_list, [
                         {'word': 'nude', 'censored': 'nud3', 'count': 1, 'indexes': [(25, 29)]}])
        self.assertEqual(filter.check(
            "I met an interesting turtle while the song on the radio blasted away.").as_list, [])
        self.assertEqual(filter.check(
            "Hello there, how are you doing today?").as_list, [])
        self.assertEqual(filter.check(
            "you wh0@r!").as_list, [{'word': 'hoar', 'censored': 'h0@r', 'count': 1, 'indexes': [(4, 8)]}, {'word': 'whore', 'censored': 'wh0r3', 'count': 1, 'indexes': [(3, 8)]}])
        self.assertEqual(filter.check(
            "The skeleton had skeletons of his own in the closet.").as_list, [])
        self.assertEqual(filter.check("You would be a great p0rn star girl!").as_list, [
                         {'word': 'porn', 'censored': 'p0rn', 'count': 1, 'indexes': [(16, 20)]}])
        self.assertEqual(filter.check(
            "They throw cabbage that turns your brain into emotional baggage.").as_list, [])
        self.assertEqual(filter.check(
            "He had concluded that pigs must be able to fly in Hog Heaven.").as_list, [])
        self.assertEqual(filter.check("Don't be scared to drop dem panties girl").as_list, [
                         {'word': 'pantie', 'censored': 'p@nt!e', 'count': 1, 'indexes': [(21, 27)]}])
        self.assertEqual(filter.check("Im good, hbu?").as_list, [])

    def filter_additions_test(self):
        filter = Filter()

        self.assertEqual(filter.check(
            "Lets go the the raveEEEEEE!!!!").as_bool, False)
        self.assertEqual(filter.check(
            "AREA 51 STATUS!!!!!!!").as_bool, False)

        filter.add_words(['rave', 'raid', 'area51', '69'])
        self.assertEqual(filter.check(
            "Pat ordered a ghost pepper pie.").as_bool, False)
        self.assertEqual(filter.check(
            "Lets go the the raveEEEEEE!!!!").as_bool, True)
        self.assertEqual(filter.check(
            "Every manager should be able to recite at least ten nursery rhymes backward.").as_bool, False)
        self.assertEqual(filter.check(
            "He took one look at what was under the table and noped the hell out of there.").as_bool, True)
        self.assertEqual(filter.check(
            "He stomped on his fruit loops and thus became a cereal killer.").as_bool, False)
        self.assertEqual(filter.check(
            "U wanna raid the new popular game?").as_bool, True)
        self.assertEqual(filter.check(
            "6666666666999999999999").as_bool, True)
        self.assertEqual(filter.check(
            "They were excited to see their first sloth.").as_bool, False)
        self.assertEqual(filter.check(
            "The tart lemonade quenched her thirst, but not her longing.").as_bool, False)
        self.assertEqual(filter.check(
            "AREA 51 STATUS!!!!!!!").as_bool, True)
        self.assertEqual(filter.check(
            "It was a really good Monday for being a Saturday.").as_bool, False)
        self.assertEqual(filter.check("42042042042000").as_bool, False)

        filter.add_words(['420'])
        self.assertEqual(filter.check("42042042042000").as_bool, True)
        self.assertEqual(filter.check("Raid time!").as_bool, True)
        self.assertEqual(filter.check(
            "The gruff old man sat in the back of the bait shop grumbling to himself as he scooped out a handful of worms.").as_bool, False)
        self.assertEqual(filter.check(
            "He realized there had been several deaths on this road, but his concern rose when he saw the exact number.").as_bool, False)
        self.assertEqual(filter.check(
            "u headed to the rave tonight?").as_bool, True)
        self.assertEqual(filter.check(
            "This made him feel like an old-style rootbeer float smells.").as_bool, False)

    def filter_exceptions_test(self):
        filter = Filter()

        self.assertEqual(filter.check(
            "what da fuuuuuuck!").as_bool, True)

        filter.add_exceptions(['fuck'])
        self.assertEqual(filter.check(
            "what da fuuuuuuck!").as_bool, True)
        self.assertEqual(filter.check("i love big asses").as_bool, True)
        self.assertEqual(filter.check(
            "why the fuck is there nobody here").as_bool, False)
        self.assertEqual(filter.check(
            "bitch what u lookin at").as_bool, True)
        self.assertEqual(filter.check("suck my dick").as_bool, True)
        self.assertEqual(filter.check(
            "Hi there, what have you been doing?").as_bool, False)
        self.assertEqual(filter.check(
            "Im doing fine myself, just working.").as_bool, False)
        self.assertEqual(filter.check(
            "this SHHHI++++ is crazy!!!!").as_bool, True)
        self.assertEqual(filter.check(
            "why are we even still friends?").as_bool, False)
        self.assertEqual(filter.check(
            "u an asshole mate").as_bool, True)

        filter.add_exceptions(['bitch', 'asshole'])
        self.assertEqual(filter.check(
            "bitch what u lookin at").as_bool, False)
        self.assertEqual(filter.check(
            "bitch look at yourself").as_bool, False)
        self.assertEqual(filter.check("Eat my shi+!").as_bool, True)
        self.assertEqual(filter.check(
            "u an asshole mate").as_bool, False)
        self.assertEqual(filter.check(
            "what the Fuck you think your up to?").as_bool, False)
        self.assertEqual(filter.check(
            "Why is there so much hatred in the world nowadays?").as_bool, False)
        self.assertEqual(filter.check(
            "Where is everyone?").as_bool, False)
        self.assertEqual(filter.check(
            "I turned 18 today!! Finally an adult!").as_bool, False)
        self.assertEqual(filter.check(
            "This person is crazzzzy!").as_bool, False)

    def custom_filter_test(self):
        filter = Filter(word_list=['testing', 'check', 'wtf', 'how u'])

        self.assertEqual(filter.check("fuck").as_bool, False)
        self.assertEqual(filter.check("bitch").as_bool, False)
        self.assertEqual(filter.check("ass").as_bool, False)
        self.assertEqual(filter.check("nigger").as_bool, False)
        self.assertEqual(filter.check("dildo").as_bool, False)
        self.assertEqual(filter.check("testing").as_bool, True)
        self.assertEqual(filter.check("check").as_bool, True)
        self.assertEqual(filter.check("wtf").as_bool, True)
        self.assertEqual(filter.check("how u").as_bool, True)
        self.assertEqual(filter.check("shit").as_bool, False)
        self.assertEqual(filter.check("pussy").as_bool, False)
        self.assertEqual(filter.check("dick").as_bool, False)

    def custom_file_test(self):
        filter = Filter(list_file='./tests/file_test.json')

        self.assertEqual(filter.check("fuck").as_bool, False)
        self.assertEqual(filter.check("bitch").as_bool, False)
        self.assertEqual(filter.check("ass").as_bool, False)
        self.assertEqual(filter.check("nigger").as_bool, False)
        self.assertEqual(filter.check("dildo").as_bool, False)
        self.assertEqual(filter.check("testing").as_bool, True)
        self.assertEqual(filter.check("check").as_bool, True)
        self.assertEqual(filter.check("wtf").as_bool, True)
        self.assertEqual(filter.check("how u").as_bool, True)
        self.assertEqual(filter.check("shit").as_bool, False)
        self.assertEqual(filter.check("pussy").as_bool, False)
        self.assertEqual(filter.check("dick").as_bool, False)


if __name__ == '__main__':
    unittest.main()
