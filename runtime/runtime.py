from agents import Runner


class AgentRuntime:

    def __init__(
            self,
            agent,
            session,
            context,
            hooks,
    ):
        self.agent = agent
        self.session = session
        self.context = context
        self.hooks = hooks

    def run_streamed(self, input):

        return Runner.run_streamed(
            starting_agent=self.agent,
            input=input,
            session=self.session,
            context=self.context,
        )