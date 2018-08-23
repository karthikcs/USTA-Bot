from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
# from rasa_core.channels.slack import SlackInput
from slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/current')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-420470916805-419761592033-419613831712-da50b70570d99d6981b66723d8fb8391',
'xoxb-420470916805-419613833632-VIj1Nptcr2x5FqpKrlNlmotc',
'dhwYIumHCA9QLesY6FQ1zsz8', True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))