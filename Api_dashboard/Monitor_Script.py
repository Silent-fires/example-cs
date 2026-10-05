import time
import sys
#from unitree_sdk2_python.core.channel import ChannelSubscriber, ChannelFactory
# Import the specific message IDL types depending on your Unitree model
#from unitree_sdk2_python.idl.default import SportModeState_
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactory
from unitree_sdk2py.idl.default import SportModeState_

def topic_callback(msg):
    # Print the specific values coming over the wire 
    print(f"Position: {msg.position}, Velocity: {msg.velocity}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 monitor.py [Network_Interface_Name (e.g. eth0)]")
        sys.exit(0)
        
    # Initialize the Channel Factory to look at your network interface
    ChannelFactory.Initialize(0, sys.argv[1])
    
    # Subscribe to the Sport Mode state topic (e.g., for Go2/G1 tracking)
    # The topic name usually takes the format "rt/sportmodestate"
    sub = ChannelSubscriber("rt/sportmodestate", SportModeState_)
    sub.InitChannel(topic_callback)
    
    print("Listening for Unitree SDK2 topics... Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting.")

