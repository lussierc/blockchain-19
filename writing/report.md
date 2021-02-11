# Report by Ryan Hilty, Christian Lussier, Jordan Wilson

## Introduction and Motivation

What is the concept behind your project? How does it satisfy the two broad requirements on this assignments? Discuss briefly
how your concept is motivated by the cryptocurrency-related technology and what existing or potential solutions might it provide to our challenges?

Throughout the last three weeks our class have had an in depth discussion about cryptocurrencies and how they function. The algorithm behind one of the biggest 
cyrptocurrencies (bitcoin) is known as blockchain. Blockchain was one of the main focus points in our class sessions as it is the key to creating and correcting the 
ledger that bitcoin runs on. This algorithm allows storage of the mining and transaction of bitcoin across the globe, a decentralized system that allows anyone to 
confirm and work with each other, while also keeping all individual parties anonymous. Blockchain is a great data way to store data and recall on those data points. 
With all that we had learned over the semester we knew that a blockchain data storage algorithm based program is what our group wanted to pursue. The only thing we 
needed to create our algorithm was data to store in it. We thought about this for a few days as the data is almost as important as the algorithm its being stored 
in. With all of the data and research with the current global pandemic, we wanted to use mock-up covid-19 hospital / patient data. This direction was realistic in 
the way that our algorithm could store important data for hospitals and researchers without giving away the identity of any patients. Patient confidentiality is 
important to the integrity of our healthcare system, which made blockchain storage a perfect fit for this realistic application. Here is where Blockchain-19 was 
started. 

## Design of your Project

This section should provide detailed description of your design. Please include a visual representation of the design of your project. This could include a technical diagram or a flowchart demonstrating how your concept works, a walk through a conceptual example, etc. 

Now that we had our idea set in stone we needed to hash out (pun intended) how we were going to design and move forward with the project. There were several steps 
going forward before we started implementing our algorithm. The group needed to layout how the functionality of the program would work, what variables were we 
using, how was the hash going to be generated, where are we storing variables, etc. When we first started thinking about the flow of our program we ran into some 
functionalities that we wanted the program to have. As listed in the flow chart below, we wanted the user to have the option to start a new ledger or import and 
existing one. This would allow for integrity of the data as the user is now able to save data entered and enter new data without the risk of losing or entangling 
old data. 

![alt text](https://github.com/allegheny-computer-science-390-f2020/project-blockchain19/blob/main/resources/ProgramCycle.png)

This was important to the functionality of the program and for application purposes. Now if a researcher or doctor is looking at the ledger they have an option to c
continue the blockchain of old files, or start a new one for say 'a patient overload'. This small function made the program more dynamic and have a more realistic 
applicable use. 

Once the user selects whether to import or export the desired ledger, they will have to enter the information block by block, each patient being one block. The 
information that the computer needs to solve for the hash is the Patient ID, Hopsital ID, and Patient Status. These are the three variables (a,b,c) in our hash 
function that are required to calculate the hash variable. We used the equation below to calculate our hash function. 

![alt text](https://github.com/allegheny-computer-science-390-f2020/project-blockchain19/blob/main/resources/HashFunction.png)

This was the basic function we used to solve for all of our hash values in the blockchain algorithm. Using this equation the program is able to store and call on 
any of those variables after the hash is calculated. Once the hash is calcluated, the program would simply take the next input and calculate the next hash. All of 
the hash functions are connected to each other, keeping the integrity of the blockchain. This must be kept in mind during implementation so that we made sure the 
correct values were passed to the next hash, avoiding errors in calculation. To make sure the algorithm and function worked, and for our own basic understanding of how the function needed to be solved, the group individually calculated the mock-values below.

![alt text](https://github.com/allegheny-computer-science-390-f2020/project-blockchain19/blob/main/resources/Chart.png)

This file was a great resource for our implementation. Creating this file was important for the understanding of how the group was going to implement this design. 
When it was time to implement this part of the project, the chart made it much simplier to understand. The implementation was a bit tricky as there are a lot of 
calculations and numbers being stored. Correctly passing these values on was key to having the correct output. 

## Implementation

This section should describe implementation details of your project (how you implemented your solution). Please describe which languages, libraries, external tools you used. This section should also provide commands (in code blocks) that are needed to run your implementation and what is needed to be installed beforehand. 

For the implementation of our project we decided to use the python programming language for its libraries and out prior 
knowledge of the language. The main libraries that we used in our python program were: CSV, PRETTY Table, and RE. These 
allowed us to import and export files, format our document output, and use ascii values for our created hash function. Our original program was all set in one file, but now we have our program running out of 5 files: blockchain19.py / csv_handler.py / hash_calcs.py / ledger_handler.py / print_content.py. blockchain19.py is the main function when the main function runs it will use the user input to decide the next step. The user can select to import a old ledger, create a new ledger, or look at the information center. The inforomation center is shown below:

![alt text](Information Center)

This gives a little bit of detail about the program and some of the hash values that go along in it. If the user chooses 
to import and old ledger, it will prompt for the file name. If the file is found, it will open and allow the user to 
start editing the previous ledger. If the user chooses to create a new ledger they will be prompted to enter the 
Hopsital Name, Patient ID, and Patient status. It will then ask if there are more blocks to be entered and depending on 
the user input they will decide whether to enter more data or not. Once the data is completely entered, the program will print a table with all of the data as shown below. 

![alt text](Prompted Data and file print)

Each file handles an important part of the program. We needed to break up our larger file as it was becoming cluttered and difficult to comprehend. 
When looking at all of the files, the hash_calcs.py is the function that calculates the hash function. Given a new ledger the file sets the values to 
0 and starts taking user input. To find the ascii values, we used the 'first_letter' function. This takes the first letter value in the user entered 
string data and converts it to its correspsonding ascii value. This is crucial to be correct or else all of the calculations will be off for the 
entire ledger. The new ascii values are added together and subtracted from the prev_hash and stored into a variable. The progrma then calls on the 
'find_nonce' function. This function runs a simple for loop, running at a max of three times to see if the intermediate hash and the nonce are 
divisible by 3. We used the 'is_integer' function to determine when a whole numbered was returned. Once this number was found, we stored and returned 
the nonce. This value is then added to our intermediate hash, and stored in the new hash variables. This is our final hash for this block. Once the 
hash is found the variables were store into a block feature and then printed for the user. If there are more hash block functions to solve, the 
program will continue to run through this procedure until there are no more blocks found from the user input. 

## Evaluation and Testing

This section should concentrate on how you conducted evaluation of your solution. You should test your implementation with different inputs (at least ten, if it makes sense) to verify its correctness, efficiency, effectiveness, etc. as appropriate for your project. Please include the input and a sample output in code blocks or indicate where these inputs/outputs are located  (as appropriate given your implementation). Automated testing is preferred but manual testing is acceptable. You must describe the type of testing that have been done and include the output of test cases in code blocks if appropriate.

## Description of the challenges that you faced and how you resolved them

## If worked in a team, description of the way in which you and your team members shared the project work

