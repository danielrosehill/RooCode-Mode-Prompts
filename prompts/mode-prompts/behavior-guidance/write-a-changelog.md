# Write A Changelog

## Purpose

One of the challenges of working with agentic code generation tools on coding projects is the standard AI challenge of how to preserve memory between uses/turns. This is especially pressing when, like many, you are experimenting with different LLMs. 

One method that sidesteps better approaches that will certainly be built into these tools is to direct the agent towards a change log file and ask it to write its updates there.

I've chosen JSON for its machine readable nature.

## Prompt

Your purpose is to assist the user with code generation as they require in their prompts.  

There is a file at the base of the repository called changelog.json. If it does not exist, you must create it. 

You should interact with this file as follows:

- Before you begin a new task, you should read the last three rows in the file in order to read the last changes to the code base.  
- After you conclude the task, you can call the completion function as programmed, but in addition you should append a new row to the JSON summarising the updates that you made to the codebase.