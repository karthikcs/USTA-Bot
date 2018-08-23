from rasa_core.interpreter import RasaNLUInterpreter
import logging, io, json, warnings

def pprint(o):
    # small helper to make dict dumps a bit prettier
    print(json.dumps(o, indent=2))

interpreter = RasaNLUInterpreter("models/nlu/default/current")
pprint(interpreter.parse("search candidates with Ajax skills"))
