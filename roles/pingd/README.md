pingd is a forked repository containing a collection composed of:
- a role, pingd, that pings dependending on the os and for linux uses pingdl python custom module instead of ping module
- a module, pingDL is forked based on ansible standard ping module and only replaces ping pong by tic tac which obviously does not work (dummy module, I should have named it tic module)
All this said its only aim is to showcase the use of galaxy ant its limitations. Collections make it easy to deliver modules also with the roles.
