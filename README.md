# RooCode Mode Prompts: My Collection

 This repository contains my collection of mode prompts and role prompts for [Roo Code](https://github.com/RooVetGit/Roo-Code) (previously: Roo Cline).

Just like any other system prompt, mode prompts are deceptively simple but highly powerful text configurations which can alter the functionality, performance and feel of the agentic tool. 

## Role Prompts, Mode Prompts

A huge benefit of Roo Code is the fact that it allows users to create as many personal prompts as they wish to guide the tool to behaving as they wish. 

Your prompts can be workspace-level-specific by adding them at:

`/home/daniel/Development/git-repositories/My-Repos/RooCode-Mode-Prompts/.clinerules-code`

Or they can be "global" - meaning that they will hold throughout whatever you're working on in the IDE.

## Role  -> Mode 

My understanding of the role and mode prompt hierarchy is something like this (for more precise definitions, see the project's docs):

- The "role" prompt directs the overall *function* of the agent 
- The "mode" prompt alllows you to tweak the *nuances* of that behavior  

This segmentation makes a lot of sense!

The agent can be (first and foremost) a coding agent (the classic use-case) with modes for discrete tasks like debugging Python or writing Java. 

Or it can be (first and foremost) a documentation agent. 

I try to think of it like this:

Each role config transforms Roo into a different team member in your imaginary coding assistance startup. The "mode" determines what that team member actually does at any given point in time. 

For that reason I (personally):

- Have only a few role prompts  
- Am working on quite a lot of targeted mode prompts to be able to quickly zone in Roo on specific tasks without having to prompt the same instructions over and over again  

Therefore, to create modes (a mode having both a role and mode prompt):

- Add one role prompt  
- Add one mode prompt  

## My Prompts-As-Docs Approach 
 
 I have developed (I'm waiting on the patent - JK!) my own method for writing prompts as documents and then providing them as context to Cline / Roo Code / etc. I call this approach *"prompts as docs"*. 

It can be used with or without a mode/system prompt. The latter can be used to tell the overall prompt guiding Roo Code not to consider the "prompt docs" to be part of the codebase or to use them as context for coding unless explicitly instructed to do so. 

The `read-prompt-docs` folder contains a few prompts for this purpose. 

## JSON Exports

I will periodically copy my own `JSON` config file into the repository for anyone who would like to import some of the configs in that way

---

## Author

Daniel Rosehill  
(public at danielrosehill dot com)

## Licensing

This repository is licensed under CC-BY-4.0 (Attribution 4.0 International) 
[License](https://creativecommons.org/licenses/by/4.0/)

### Summary of the License
The Creative Commons Attribution 4.0 International (CC BY 4.0) license allows others to:
- **Share**: Copy and redistribute the material in any medium or format.
- **Adapt**: Remix, transform, and build upon the material for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the license terms.

#### License Terms
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **No additional restrictions**: You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For the full legal code, please visit the [Creative Commons website](https://creativecommons.org/licenses/by/4.0/legalcode).