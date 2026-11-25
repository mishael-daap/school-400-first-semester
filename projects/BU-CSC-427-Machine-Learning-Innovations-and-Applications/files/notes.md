anatomy of a contaxt aware ageint 

llm
system pronmpt: the agents persona tome and dulrs sent with every request
knowledge base: you r documents seached at question time so answers are grounded facts
conversation memory: previous turns so that questions based on past messages make sense
guardrails: keep it on itt' predetermined topics and refuse the rest politely
interface: where the userst talk to the agent

rule based chatbot 
it matehces kewords or intents

# whwere chatbots go wrong

# hallucination 
- confidently invets facts
- *fix*: ground answers in a knowledge base and allow i dont know

# topic drift
- A study bot writing poems and giving medical advice
- *Fix*: clear in scopt and out of scope topics 

# Forgets the conversation 
each message treated alone
fix: design for memory from day one

# unsafe or leaky 
- reveals it's prompt, follows malicious instructions
- fix: guardrails and testing

# agent scoping canvas 

users: who talks to it what do they already know and what device do they use 
jobs to be done: the three to 5 things most users need help with 
in scope topics: the predetermined topics it will discus be specific
out of scope: what it must decline and what says instead
knowledeg source: where answers come from and who owns it and is reuse allowed
persona and tone: formal or friendly, short or detailed, which language? 

founctional vs non functional requirements 
functional: what it does
non functional: how well it does it

design the conversation first
write golden conversations before code, they become your spec and your tests 

happy path: a typical question answered with a source
follow up: relies on the thoury of the previous turn
out of scope: a polite helpful refusal

turning requirements into success metrics


my question: 
when you are building an application that deals with sensitive information for example customers nin, how do you ensure that the agent can retrieve and work with that piece of information without actually reading it the information
