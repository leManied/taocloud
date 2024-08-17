# The MIT License (MIT)
# Copyright © 2023 Damien Thumerel
# With contributions from the Bittensor Community, inspired by Subvortex codebase.

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import time
import typing
import bittensor as bt
import threading
import torch
import sys
import io





class Miner:
    @classmethod
    def check_config(cls, config: "bt.Config"):
        """
        Adds neuron-specific arguments to the argument parser.

        Args:
            parser (argparse.ArgumentParser): Parser to add arguments to.

        This class method enriches the argument parser with options specific to the neuron's configuration.
        """
        check_config(cls, config)

    @classmethod
    def add_args(cls, parser):
        """
        Adds neuron-specific arguments to the argument parser.

        Args:
            parser (argparse.ArgumentParser): Parser to add arguments to.

        This class method enriches the argument parser with options specific to the neuron's configuration.
        """
        add_args(cls, parser)

    @classmethod
    def config(cls):
        """
        Retrieves the configuration for the neuron.

        Returns:
            bt.Config: The configuration object for the neuron.

        This class method returns the neuron's configuration, which is used throughout the neuron's lifecycle
        for various functionalities and operations.
        """
        return config(cls)

    subtensor: "bt.subtensor"
    wallet: "bt.wallet"
    metagraph: "bt.metagraph"
    

    def __init__(self):

        #TODO: Implement the initialization of the connection to bt.subtensor and wait for the connection to be established
        #TODO: Implement the initialization of the bt.axon and annonce the axon to validators
        #TODO: Create the folder for the miner's data

    def run_in_background_thread():
        print("Miner started")
        #TODO : 
        
        


def run_miner():
    """
    Main function to run the neuron.

    This function initializes and runs the neuron. It handles the main loop, state management, and interaction
    with the Bittensor network.
    """
    miner = None
    try:
        miner = Miner()
        miner.run_in_background_thread()

        while 1:
            time.sleep(1)
    except KeyboardInterrupt:
        bt.logging.info("Keyboard interrupt detected, exiting.")
        sys.exit(0)
    except Exception as e:
        bt.logging.error(traceback.format_exc())
        bt.logging.error(f"Unhandled exception: {e}")
        sys.exit(1)
    finally:
        if miner:
            bt.logging.info("Stopping axon")
            miner.axon.stop()


if __name__ == "__main__":
    run_miner()