import unittest
import content_filter


class TestFilter(unittest.TestCase):
    def accuracy_test(self):
        self.assertEqual(content_filter.checkMessage("FUCK YOU BITCH"), True)
        self.assertEqual(content_filter.checkMessage(
            "Hi there, how are you doing today?"), False)
        self.assertEqual(content_filter.checkMessage("Im good, hbu?"), False)
        self.assertEqual(content_filter.checkMessage(
            "I'm good, how about you?"), False)
        self.assertEqual(content_filter.checkMessage(
            "The small white buoys marked the location of hundreds of crab pots."), False)
        self.assertEqual(content_filter.checkMessage("what da fuck"), True)
        self.assertEqual(content_filter.checkMessage("eat my ass"), True)
        self.assertEqual(content_filter.checkMessage(
            "The ants enjoyed the barbecue more than the family."), False)
        self.assertEqual(content_filter.checkMessage(
            "Car safety systems have come a long way, but he was out to prove they could be outsmarted."), False)
        self.assertEqual(content_filter.checkMessage(
            "At that moment he wasn't listening to music, he was living an experience."), False)
        self.assertEqual(content_filter.checkMessage(
            "He invested some skill points in Charisma and Strength."), False)
        self.assertEqual(content_filter.checkMessage(
            "He wore the surgical mask in public not to keep from catching a virus, but to keep people away from him."), False)
        self.assertEqual(content_filter.checkMessage(
            "Peanut butter and jelly caused the elderly lady to think about her past."), False)
        self.assertEqual(content_filter.checkMessage(
            "He found the chocolate covered roaches quite tasty."), False)
        self.assertEqual(content_filter.checkMessage(
            "I currently have 4 windows open up… and I don’t know why."), False)
        self.assertEqual(content_filter.checkMessage(
            "The efficiency we have at removing trash has made creating trash more acceptable."), False)
        self.assertEqual(content_filter.checkMessage(
            "Chocolate covered crickets were his favorite snack."), False)
        self.assertEqual(content_filter.checkMessage(
            "He stepped gingerly onto the bridge knowing that enchantment awaited on the other side."), False)
        self.assertEqual(content_filter.checkMessage(
            "25 years later, she still regretted that specific moment."), False)
        self.assertEqual(content_filter.checkMessage(
            "They wandered into a strange Tiki bar on the edge of the small beach town."), False)
        self.assertEqual(content_filter.checkMessage(
            "I like to suck d***"), True)
        self.assertEqual(content_filter.checkMessage(
            "what os this $h!+"), True)
        self.assertEqual(content_filter.checkMessage(
            "I'm confused: when people ask me what's up, and I point, they groan."), False)
        self.assertEqual(content_filter.checkMessage(
            "It's difficult to understand the lengths he'd go to remain short."), False)
        self.assertEqual(content_filter.checkMessage(
            "Each person who knows you has a different perception of who you are."), False)
        self.assertEqual(content_filter.checkMessage(
            "It would have been a better night if the guys next to us weren't in the splash zone."), False)
        self.assertEqual(content_filter.checkMessage(
            "His thought process was on so many levels that he gave himself a phobia of heights."), False)
        self.assertEqual(content_filter.checkMessage(
            "While on the first date he accidentally hit his head on the beam."), False)
        self.assertEqual(content_filter.checkMessage(
            "He decided that the time had come to be stronger than any of the excuses he'd used until then."), False)
        self.assertEqual(content_filter.checkMessage("got any d!ld0s?"), True)
        self.assertEqual(content_filter.checkMessage(
            "When I was little I had a car door slammed shut on my hand and I still remember it quite vividly."), False)
        self.assertEqual(content_filter.checkMessage(
            "I checked to make sure that he was still alive."), False)
        self.assertEqual(content_filter.checkMessage(
            "The beauty of the sunset was obscured by the industrial cranes."), False)
        self.assertEqual(content_filter.checkMessage(
            "The near-death experience brought new ideas to light."), False)
        self.assertEqual(content_filter.checkMessage(
            "The truth is that you pay for your lifestyle in hours."), False)
        self.assertEqual(content_filter.checkMessage(
            "The view from the lighthouse excited even the most seasoned traveler."), False)
        self.assertEqual(content_filter.checkMessage(
            "He found the end of the rainbow and was surprised at what he found there."), False)
        self.assertEqual(content_filter.checkMessage(
            "She finally understood that grief was her love with no place for it to go."), False)
        self.assertEqual(content_filter.checkMessage(
            "u got a nice pu$$y girl?"), True)
        self.assertEqual(content_filter.checkMessage(
            "go to he!l you idiot"), True)
        self.assertEqual(content_filter.checkMessage(
            "There aren't enough towels in the world to stop the sewage flowing from his mouth."), False)
        self.assertEqual(content_filter.checkMessage(
            "Swim at your own risk was taken as a challenge for the group of Kansas City college students."), False)
        self.assertEqual(content_filter.checkMessage(
            "She had a habit of taking showers in lemonade."), False)
        self.assertEqual(content_filter.checkMessage(
            "He was 100% into fasting with her until he understood that meant he couldn't eat."), False)
        self.assertEqual(content_filter.checkMessage(
            "On a scale from one to ten, what's your favorite flavor of random grammar?"), False)
        self.assertEqual(content_filter.checkMessage(
            "25 years later, she still regretted that specific moment."), False)
        self.assertEqual(content_filter.checkMessage(
            "He waited for the stop sign to turn to a go sign."), False)
        self.assertEqual(content_filter.checkMessage(
            "oh girl giv me dem t1+s"), True)
        self.assertEqual(content_filter.checkMessage(
            "How about you shows me your b00b$ tonight?"), True)
        self.assertEqual(content_filter.checkMessage(
            "Lets have $3x tonight baby girl?"), True)
        self.assertEqual(content_filter.checkMessage(
            "Im gonna rap3 you little girl"), True)
        self.assertEqual(content_filter.checkMessage(
            "He had concluded that pigs must be able to fly in Hog Heaven."), False)
        self.assertEqual(content_filter.checkMessage(
            "We have a lot of rain in June."), False)
        self.assertEqual(content_filter.checkMessage(
            "He quietly entered the museum as the super bowl started."), False)
        self.assertEqual(content_filter.checkMessage(
            "I am happy to take your donation; any amount will be greatly appreciated."), False)
        self.assertEqual(content_filter.checkMessage(
            "Potato wedges probably are not best for relationships."), False)
        self.assertEqual(content_filter.checkMessage(
            "You're unsure whether or not to trust him, but very thankful that you wore a turtle neck."), False)
        self.assertEqual(content_filter.checkMessage(
            "He picked up trash in his spare time to dump in his neighbor's yard."), False)
        self.assertEqual(content_filter.checkMessage(
            "At that moment she realized she had a sixth sense."), False)
        self.assertEqual(content_filter.checkMessage(
            "You would be a great p0rn star girl!"), True)
        self.assertEqual(content_filter.checkMessage(
            "Charles ate the french fries knowing they would be his last meal."), False)
        self.assertEqual(content_filter.checkMessage(
            "Let me insert myself into that vjayjay girl"), True)
        self.assertEqual(content_filter.checkMessage(
            "Don't be scared to drop dem panties girl"), True)
        self.assertEqual(content_filter.checkMessage(
            "Make sure to lube up your vaj before we get down"), True)
        self.assertEqual(content_filter.checkMessage(
            "The opportunity of a lifetime passed before him as he tried to decide between a cone or a cup."), False)
        self.assertEqual(content_filter.checkMessage(
            "She tilted her head back and let whip cream stream into her mouth while taking a bath."), False)
        self.assertEqual(content_filter.checkMessage(
            "They throw cabbage that turns your brain into emotional baggage."), False)
        self.assertEqual(content_filter.checkMessage(
            "The newly planted trees were held up by wooden frames in hopes they could survive the next storm."), False)
        self.assertEqual(content_filter.checkMessage(
            "She says she has the ability to hear the soundtrack of your life."), False)
        self.assertEqual(content_filter.checkMessage(
            "We have young kids who often walk into our room at night for various reasons including clowns in the closet."), False)
        self.assertEqual(content_filter.checkMessage(
            "It's much more difficult to play tennis with a bowling ball than it is to bowl with a tennis ball."), False)
        self.assertEqual(content_filter.checkMessage(
            "Most shark attacks occur about 10 feet from the beach since that's where the people are."), False)
        self.assertEqual(content_filter.checkMessage(
            "Of course, she loves her pink bunny slippers."), False)
        self.assertEqual(content_filter.checkMessage(
            "It didn't make sense unless you had the power to eat colors."), False)
        self.assertEqual(content_filter.checkMessage(
            "After exploring the abandoned building, he started to believe in ghosts."), False)
        self.assertEqual(content_filter.checkMessage(
            "He learned the important lesson that a picnic at the beach on a windy day is a bad idea."), False)
        self.assertEqual(content_filter.checkMessage(
            "The shark-infested South Pine channel was the only way in or out."), False)
        self.assertEqual(content_filter.checkMessage(
            "The skeleton had skeletons of his own in the closet."), False)
        self.assertEqual(content_filter.checkMessage(
            "He was willing to find the depths of the rabbit hole in order to be with her."), False)
        self.assertEqual(content_filter.checkMessage("you wh0@r!"), True)
        self.assertEqual(content_filter.checkMessage(
            "He didn’t want to go to the dentist, yet he went anyway."), False)
        self.assertEqual(content_filter.checkMessage(
            "Girl, r u a h0ok3r?"), True)
        self.assertEqual(content_filter.checkMessage(
            "lets get naked up in here"), True)
        self.assertEqual(content_filter.checkMessage(
            "Check back tomorrow; I will see if the book has arrived."), False)
        self.assertEqual(content_filter.checkMessage(
            "I would be delighted if the sea were full of cucumber juice."), False)
        self.assertEqual(content_filter.checkMessage(
            "Even though he thought the world was flat he didn’t see the irony of wanting to travel around the world."), False)
        self.assertEqual(content_filter.checkMessage(
            "Lets all be unique together until we realise we are all the same."), False)
        self.assertEqual(content_filter.checkMessage(
            "Hit me with your pet shark!"), False)
        self.assertEqual(content_filter.checkMessage(
            "I met an interesting turtle while the song on the radio blasted away."), False)
        self.assertEqual(content_filter.checkMessage(
            "You always look best when your nude!"), True)
        self.assertEqual(content_filter.checkMessage(
            "Be careful with that butter knife."), False)
        self.assertEqual(content_filter.checkMessage(
            "I am my aunt's sister's daughter."), False)
        self.assertEqual(content_filter.checkMessage(
            "Toddlers feeding raccoons surprised even the seasoned park ranger."), False)
        self.assertEqual(content_filter.checkMessage(
            "FFFFFFFFFFUUUUUUUUUUUUUUUUUUUUUUCCCCCCCCCCKKKKKKKKKKK ME!!!!!"), True)
        self.assertEqual(content_filter.checkMessage(
            "She wondered what his eyes were saying beneath his mirrored sunglasses."), False)
        self.assertEqual(content_filter.checkMessage(
            "The lyrics of the song sounded like fingernails on a chalkboard."), False)
        self.assertEqual(content_filter.checkMessage(
            "Nothing seemed out of place except the washing machine in the bar."), False)
        self.assertEqual(content_filter.checkMessage(
            "When transplanting seedlings, candied teapots will make the task easier."), False)
        self.assertEqual(content_filter.checkMessage(
            "He learned the hardest lesson of his life and had the scars, both physical and mental, to prove it."), False)
        self.assertEqual(content_filter.checkMessage(
            "You bite up because of your lower jaw."), False)
        self.assertEqual(content_filter.checkMessage(
            "The mysterious diary records the voice."), False)
        self.assertEqual(content_filter.checkMessage(
            "Hello there, how are you doing today?"), False)
        self.assertEqual(content_filter.checkMessage("scunthorpe"), False)

    def filter_list_test(self):
        self.assertEqual(content_filter.checkMessageList("You always look best when your nude!"), [
                         {'word': 'nude', 'censored': 'nud3', 'count': 1}])
        self.assertEqual(content_filter.checkMessageList(
            "I met an interesting turtle while the song on the radio blasted away."), [])
        self.assertEqual(content_filter.checkMessageList(
            "Hello there, how are you doing today?"), [])
        self.assertEqual(content_filter.checkMessageList(
            "you wh0@r!"), [{'word': 'hoar', 'censored': 'h0@r', 'count': 1}, {'word': 'whore', 'censored': 'wh0r3', 'count': 1}])
        self.assertEqual(content_filter.checkMessageList(
            "The skeleton had skeletons of his own in the closet."), [])
        self.assertEqual(content_filter.checkMessageList("You would be a great p0rn star girl!"), [
                         {'word': 'porn', 'censored': 'p0rn', 'count': 1}])
        self.assertEqual(content_filter.checkMessageList(
            "They throw cabbage that turns your brain into emotional baggage."), [])
        self.assertEqual(content_filter.checkMessageList(
            "He had concluded that pigs must be able to fly in Hog Heaven."), [])
        self.assertEqual(content_filter.checkMessageList("Don't be scared to drop dem panties girl"), [
                         {'word': 'pantie', 'censored': 'p@nt!e', 'count': 1}])
        self.assertEqual(content_filter.checkMessageList("Im good, hbu?"), [])

    def filter_additions_test(self):
        self.assertEqual(content_filter.checkMessage(
            "Lets go the the raveEEEEEE!!!!"), False)
        self.assertEqual(content_filter.checkMessage(
            "AREA 51 STATUS!!!!!!!"), False)

        content_filter.addWords(['rave', 'raid', 'area51', '69'])
        self.assertEqual(content_filter.checkMessage(
            "Pat ordered a ghost pepper pie."), False)
        self.assertEqual(content_filter.checkMessage(
            "Lets go the the raveEEEEEE!!!!"), True)
        self.assertEqual(content_filter.checkMessage(
            "Every manager should be able to recite at least ten nursery rhymes backward."), False)
        self.assertEqual(content_filter.checkMessage(
            "He took one look at what was under the table and noped the hell out of there."), True)
        self.assertEqual(content_filter.checkMessage(
            "He stomped on his fruit loops and thus became a cereal killer."), False)
        self.assertEqual(content_filter.checkMessage(
            "U wanna raid the new popular game?"), True)
        self.assertEqual(content_filter.checkMessage(
            "6666666666999999999999"), True)
        self.assertEqual(content_filter.checkMessage(
            "They were excited to see their first sloth."), False)
        self.assertEqual(content_filter.checkMessage(
            "The tart lemonade quenched her thirst, but not her longing."), False)
        self.assertEqual(content_filter.checkMessage(
            "AREA 51 STATUS!!!!!!!"), True)
        self.assertEqual(content_filter.checkMessage(
            "It was a really good Monday for being a Saturday."), False)
        self.assertEqual(content_filter.checkMessage("42042042042000"), False)

        content_filter.addWords('420')
        self.assertEqual(content_filter.checkMessage("42042042042000"), True)
        self.assertEqual(content_filter.checkMessage("Raid time!"), True)
        self.assertEqual(content_filter.checkMessage(
            "The gruff old man sat in the back of the bait shop grumbling to himself as he scooped out a handful of worms."), False)
        self.assertEqual(content_filter.checkMessage(
            "He realized there had been several deaths on this road, but his concern rose when he saw the exact number."), False)
        self.assertEqual(content_filter.checkMessage(
            "u headed to the rave tonight?"), True)
        self.assertEqual(content_filter.checkMessage(
            "This made him feel like an old-style rootbeer float smells."), False)

    def filter_exceptions_test(self):
        self.assertEqual(content_filter.checkMessage(
            "what da fuuuuuuck!"), True)

        content_filter.addExceptions('fuck')
        self.assertEqual(content_filter.checkMessage(
            "what da fuuuuuuck!"), True)
        self.assertEqual(content_filter.checkMessage("i love big asses"), True)
        self.assertEqual(content_filter.checkMessage(
            "why the fuck is there nobody here"), False)
        self.assertEqual(content_filter.checkMessage(
            "bitch what u lookin at"), True)
        self.assertEqual(content_filter.checkMessage("suck my dick"), True)
        self.assertEqual(content_filter.checkMessage(
            "Hi there, what have you been doing?"), False)
        self.assertEqual(content_filter.checkMessage(
            "Im doing fine myself, just working."), False)
        self.assertEqual(content_filter.checkMessage(
            "this SHHHI++++ is crazy!!!!"), True)
        self.assertEqual(content_filter.checkMessage(
            "why are we even still friends?"), False)
        self.assertEqual(content_filter.checkMessage(
            "u an asshole mate"), True)

        content_filter.addExceptions(['bitch', 'asshole'])
        self.assertEqual(content_filter.checkMessage(
            "bitch what u lookin at"), False)
        self.assertEqual(content_filter.checkMessage(
            "bitch look at yourself"), False)
        self.assertEqual(content_filter.checkMessage("Eat my shi+!"), True)
        self.assertEqual(content_filter.checkMessage(
            "u an asshole mate"), False)
        self.assertEqual(content_filter.checkMessage(
            "what the Fuck you think your up to?"), False)
        self.assertEqual(content_filter.checkMessage(
            "Why is there so much hatred in the world nowadays?"), False)
        self.assertEqual(content_filter.checkMessage(
            "Where is everyone?"), False)
        self.assertEqual(content_filter.checkMessage(
            "I turned 18 today!! Finally an adult!"), False)
        self.assertEqual(content_filter.checkMessage(
            "This person is crazzzzy!"), False)


if __name__ == '__main__':
    unittest.main()
