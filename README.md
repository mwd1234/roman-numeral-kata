# roman-numeral-kata

# roman-numeral-kata

For this kata we will be converting Arabic numerals (1, 3, 22, etc) to Roman numerals (I, III, XXII, etc.). We will use this kata to practice our TDD skills. If you are unfamiliar with Roman numerals, you can review them [here](http://www.rapidtables.com/convert/number/roman-numerals-converter.htm).

Before we start, take a moment to think about how you might implement this algorithm without TDD. What kinds of programming constructs (looping, checks, classes, etc.) might you use? What kind of edge cases would you have to consider?

## Test 0
Before we start implementing anything, create a blank test that does nothing. Make sure you can run that test and that it passes.

## Test 1
The first test we choose in TDD can be very important. In converting Roman numerals we have a couple of possible options. We could start with 1. We could start with 5. For this kata let's start with 0. 0 is actually not defined for Roman numerals, so let's define it as an empty string.

Write the following test and make it pass: `zero returns empty string`

Remember to do the simplest possible thing that will make the test pass.

## Test 2
We want to do a small amount of work in each step. Let's pick a very small step that will start moving our algorithm forward.

Write the following test and make it pass: `1 returns I`

## Test 3
A very simple way to make the previous test pass would be to add a guard clause. Something like `if arabic == 1 return "I"`. 

Write the following test and make it pass: `5 returns V`

## Test 4
Before moving on the our next test, let's see if there is some duplication we can remove. If you have written the first three tests each as a separate test they probably all look very similar. See if you can make it easier to add new inputs by removing duplication. Some testing frameworks have a way to supply different test values to a common piece of test code. See if you testing framework has such an option and use if available. If not, write your own code to make adding new test values easy.

With that done, make sure all your tests still pass. If they do, let's continue moving our algorithm forward with a small amount of work.

Write the following test and make it pass: `10 returns X`

## Test 5
For our next test we could add another easy case (like L or C), but that wouldn't move our algorithm forward very much. At this point we can see that we will having some mappings between Arabic and Roman numerals. Let's start flushing out our duplicate numeral logic instead.

Write the following test and make it pass: `2 returns II`

Remember to do the simplest possible thing that will make the test pass.

## Test 6
Before moving to our next test, let's see if there's any refactoring we want to do. Do you have duplication in your code? Have you duplicated the "1"? Have you duplicated "I"? Can you remove the duplication? Try using recursion to get rid of your duplication.

With our duplication removed, let's see what happens if we continue down this path.

Write the following test and make it pass: `3 returns III`

Remember to see if your newly written test fails before adding code to make it pass. Does this one fail?

## Test 7
We got some iteration going with the previous test. Let's try adding some more.

Write the following test and make it pass: `20 returns XX`

## Test 8
Let's refactor again. You may have some duplication between the two areas of iteration. Remove that duplication.This will likely be a larger refactor than previous ones. If it is, try doing more than one refactor, where each refactor changes the shape of your code as little as possible.

We mentioned back on Test 5 that we will likely have a mapping between Arabic and Roman Numerals. Now is the time to make that mapping explicit in order to remove duplication.

Write the following test and make it pass: `50 returns L`

## Test 9
For all the non-subtractive cases you should now be at the point where it's just a matter of adding additional values to your mapping. But what about those pesky subtraction cases? (e.g. `4 returns IV`) We could complicate our algorithm to capture the rules about which values can be subtracted from which other values. But could there be an easier way?

Write the following test and make it pass: `4 returns IV`

Remember to do the simplest possible thing that will make the test pass.

## Finishing up
If you found a way to add the relationship between 4 and IV to your mapping, now all the remaining rules should just be a matter adding cases to your mapping. Try converting a large number like 3978 to see if all your mappings work.

Did using TDD to do this exercise result in a different solution that you were initially thinking about? If so, which solution did you like better?
