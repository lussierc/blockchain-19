# Report by Ryan Hilty, Christian Lussier, Jordan Wilson

## Introduction and Motivation

<!-- What is the concept behind your project? How does it satisfy the two broad requirements on this assignments? Discuss briefly
how your concept is motivated by the cryptocurrency-related technology and what existing or potential solutions might it provide to our challenges? -->

Throughout the last three weeks our class has had an in depth discussion about cryptocurrencies and how they function. The algorithm and means of storage behind one of the biggest
cryptocurrencies (Bitcoin) is known as blockchain. Blockchain was one of the main focus points in our class sessions as it is the key to creating and maintaining the
ledger that bitcoin runs on. This algorithm allows for the storage of the mining and transaction data of bitcoin across the globe, a decentralized system that allows anyone to
confirm the correctness of transactions and work with each other, while also keeping all individual parties anonymous. Blockchain is a great decentralized way to store data.
With all that we had learned over the semester we knew that a blockchain data storage algorithm based program is what our group wanted to pursue. The [Blockchain Game](https://www.instructables.com/The-Blockchain-Game/) we played in class was a big inspiration for our project, helping us to create the hash function and statuses that would be the basis for our blockchain. With an idea for our project now in mind, the only thing we
needed to create our blockchain algorithm was the data to store in it. We thought about this for a few days as the data is almost as important as the algorithm its being used
by. With all of the data and research with the current global pandemic, we wanted to use mock-up covid-19 hospital / patient data. This direction was realistic in
the way that our algorithm could store important data for hospitals and researchers without giving away the identity of any patients. Patient confidentiality is
important to the integrity of our healthcare system, which made blockchain storage a perfect fit for this realistic application. Data stored in such a blockchain could be used by both hospital systems and those investigating the virus alike, as researchers can use this confidential and anonymous data to learn more about the virus. Here is where Blockchain-19 was started.

## Design of your Project

<!-- This section should provide detailed description of your design. Please include a visual representation of the design of your project. This could include a technical diagram or a flowchart demonstrating how your concept works, a walk through a conceptual example, etc. -->

Now that we had our idea set in stone we needed to hash out (pun intended) how we were going to design and move forward with the project. There were several steps necessary
going forward before we started implementing our algorithm. The group needed to layout how the functionality of the program would work, what variables were we
using, how was the hash going to be generated, where are we storing variables, etc. When we first started thinking about the flow of our program we ran into some
functionalities that we wanted the program to have. As listed in the flow chart below, we wanted the user to have the option to start a new ledger or import and
existing one. This would allow for integrity of the data as the user is now able to save data entered and enter new data without the risk of losing or entangling
old data.

![alt text](https://github.com/allegheny-computer-science-390-f2020/project-blockchain19/blob/main/resources/ProgramCycle.png)

This was important to the functionality of the program and for application purposes. Now if a researcher or doctor is looking at the ledger they have an option to
continue the blockchain of old files, or start a new one for say 'a patient overload'. This small function made the program more dynamic and have a more realistic
applicable use.

When users imported a ledger they were given a variety of options to interact with the ledger. They could choose to add new patient information to the end of the blockchain. They could also choose to search for blocks containing a specific hospital, status, or patient ID within the ledger, as seen in the picture below. By adding search and append features, one could imagine how our project is similar to an actual blockchain. These functionalities would be perfect for hospital workers looking to add patient blocks or find certain patients within the hospital system, or for researchers looking to see how many patients had one specific status.

![alt text](https://github.com/allegheny-computer-science-390-f2020/project-blockchain19/blob/main/resources/search.png)

Once the user selects whether to import or create a new ledger, they will have the option to enter new patient information (or append this info if your are importing)  block by block, each patient being one block. The
information that the computer needs to solve for the hash is the Patient ID, Hospital ID, and Patient Status. These are the three variables (a,b,c) in our hash
function that are required to calculate the hash variable. We used the equation below to calculate our hash function.

![alt text](https://github.com/allegheny-computer-science-390-f2020/project-blockchain19/blob/main/resources/HashFunction.png)

This was the basic function we used to solve for all of our hash values in the blockchain algorithm. Using this equation the program is able to store and call on
any of those variables after the hash is calculated. Once the hash is calculated, the program would simply take the next input and calculate the next hash. All of
the hash functions are connected to each other, keeping the integrity of the blockchain. This must be kept in mind during implementation so that we made sure the
correct values were passed to the next hash, avoiding errors in calculation. To make sure the algorithm and function worked, and for our own basic understanding of how the function needed to be solved, the group individually calculated the mock-values below.

![alt text](https://github.com/allegheny-computer-science-390-f2020/project-blockchain19/blob/main/resources/Chart.png)

This file was a great resource for our implementation. Creating this file was important for the understanding of how the group was going to implement this design.
When it was time to implement this part of the project, the chart made it much simpler to understand. The implementation was a bit tricky as there are a lot of
calculations and numbers being stored. Correctly passing these values on was key to having the correct output.

## Implementation

<!-- This section should describe implementation details of your project (how you implemented your solution). Please describe which languages, libraries, external tools you used. This section should also provide commands (in code blocks) that are needed to run your implementation and what is needed to be installed beforehand. -->

For the implementation of our project we decided to use the python programming language for its libraries and out prior
knowledge of the language. The main libraries that we used in our python program were: CSV, Pretty Table, and RE. These
allowed us to import and export files, format our document output, and automatically gather ascii values for our created hash function. Our original program was all set in one file, but now we have our program running out of 5 files: `blockchain19.py` / `csv_handler.py` / `hash_calcs.py` / `ledger_handler.py` / `print_content.py`. This modularization makes it easier to test the program, read the code in the program, and helps to improve the efficiency. `blockchain19.py` is the main file, when the main function runs it will use the user input to decide the next step. The user can select to import an old ledger, create a new ledger, or look at the information center. The information center is shown below:

![alt text](https://github.com/allegheny-computer-science-390-f2020/project-blockchain19/blob/main/resources/info_center.png)

This gives a little bit of detail about the program and some of the hash values that go along in it. If the user chooses
to import and old ledger, it will prompt for the file name. If the file is found, it will open and allow the user to
start editing the previous ledger. If the user chooses to create a new ledger they will be prompted to enter the
Hospital Name, Patient ID, and Patient status. It will then ask if there are more blocks to be entered and depending on
the user input they will decide whether to enter more data or not. Once the data is completely entered, the program will print a table with all of the data as shown below.

![alt text](https://github.com/allegheny-computer-science-390-f2020/project-blockchain19/blob/main/resources/prompts.png)

Each file handles an important part of the program. We needed to break up our larger file as it was becoming cluttered and difficult to comprehend.
When looking at all of the files, the `hash_calcs.py` is the function that calculates the hashes. Given a new ledger the file sets the values to
0 and starts taking user input. To find the ascii values, we used the `first_letter` function. This takes the first letter value in the user entered
string data and converts it to its corresponding ascii value. This is crucial to be correct or else all of the calculations will be off for the
entire ledger. The new ascii values are added together and subtracted from the `prev_hash` and stored into a variable. The program then calls on the
`find_nonce()` function. This function runs a simple for loop, running at a max of three times to see if the intermediate hash and the nonce are
divisible by 3. We used the 'is_integer' function to determine when a whole numbered was returned. Once this number was found, we stored and returned
the nonce. This value is then added to our intermediate hash, and stored in the new hash variables. This is our final hash for this block. Once the
hashes are found the variables were store into their respective blocks which are then printed for the user. If there are more hash block functions to solve, the
program will continue to run through this procedure until there are no more blocks found from the user input.

## Evaluation and Testing

<!-- This section should concentrate on how you conducted evaluation of your solution. You should test your implementation with different inputs (at least ten, if it makes sense) to verify its correctness, efficiency, effectiveness, etc. as appropriate for your project. Please include the input and a sample output in code blocks or indicate where these inputs/outputs are located  (as appropriate given your implementation). Automated testing is preferred but manual testing is acceptable. You must describe the type of testing that have been done and include the output of test cases in code blocks if appropriate. -->

For our program to work we had to run several manual tests for our hash function. During these tests, each member would run through a set of numbers
set for the hash function with the goal of all returning the same number. This told us that our algorithm worked. After we implemented this we made
several different files for our testing. The randomness of our number generation was important to avoid collisions and make sure our program could
handle a wide variety of datasets. Throughout our first few tests, we ran into the issue of the nonce value returning incorrectly. Troubleshooting
this feature gave us some issues. Because of our manual tests, the understanding of how the hash function was being solved helped us resolve this
issue. The nonce was being divided incorrectly and passing the wrong value. We were able to pinpoint this issue and resolve it by making a minor
change in the for loop header.

We also performed automated testing on the key components of our program using Pytest to ensure their accuracy. This was done by implementing a simple Pytest test suite and setting it up using a configuration file, `confest.py`. With this, we implemented a test suite in `tests/test_hash_calcs.py` to check the `hash_calcs.py` functions. This file contains the main functions for the program which calculate hashes for ledgers. The functions tested included the `solve_ledger_hashes()`, `find_first_letter()`, `find_nonce()`, and `get_ascii()` functions. These functions make up the core functionality of the program as they calculate hashes using the Blockchain19 hash function. These functions were tested with test cases using both singular and multiple inputs to ensure their accuracy. For example, when testing the `find_nonce()` function, we tested it once using a singular input and again using a set of parameterized inputs (as supported by Pytest). Additionally, when testing the `solve_ledger_hashes()` function, parameterized testing was used to pass in a base ledger of patient information and an expected output of a solved ledger. Once the base ledger was passed into the `solve_ledger_hashes()` function, its values were tested against those of the expected output ledger to ensure the function correctly calculated the base ledger hashes. Automated testing allowed us to have confidence that our program can correctly calculate ledger hashes every time.

*Pytest Test Suite in action:*
![Pytest!](https://github.com/allegheny-computer-science-390-f2020/project-blockchain19/blob/main/resources/pytest.png)

By using a mix of manual and automated testing we were able to extensively evaluate our program while also ensuring it was correct. Without this
testing process we would have had a lot of difficulty trying to translate the hash function into the program. Learning and working through the hash
function allowed us to be able to smoothly and effectively create and implement this program.

## Challenges Faced

Some examples of the challenges that we ran into were first getting the hash function to run properly. This was a big part of our project so getting this to work properly was pretty important. In order to get the hash functions to run properly. We looked at example code that we did in class as well as hand calculating the results to make sure we were getting the correct nonces and such. Once we did a manual run through of our hash function and got the same results, we knew we implemented the program correctly. Another challenge we had ran into was testing. Since we had used Python to code our project we had to use Pytest in order to make sure our output was correct. It was a bit challenging since none of us had tested using Pytest in a while, so we referred to assignments from previous classes for inspiration and to refresh our memories. We had written test cases to find things such as first letter, nonce and ledger to make sure the results were accurate. This also helped us to ensure that our program ran properly and smoothly. The last big challenge that we had ran into was the implementation of our program. A big problem was that we had forgot to convert the lowercase letter to uppercase when calculating ascii values. Once we had implemented code that automatically converted the inputted letter for the function to uppercase, we were able to get the proper results and output of our program. Also writing a test case for this helped ensure that our program would run properly and get the desired output.

## Team Work

While working as a team on this project, we were easily able to split up the work among all group members. We were given a lot of time during class session to work on this project and each time we met during class, each member would work on the program together and we would collaboratively give suggestions on what we should and can do to implement the proper functions for our program. Also as well as during class time, all of the members of our group met outside of class to discuss what we needed to do in order to stay on schedule and add more functions to our program. Each member of our team also contributed in presenting our project to our peers when it was time to do so.

Christian helped with much of the programming while also helping to work on the presentation and report when necessary. Ryan also helped with the code while taking the lead on the report and working on the presentations. Jordan helped with both the report and code while doing much of the presentations. Overall, our team split the work evenly for the most part and we all put the same amount of time into the project.
