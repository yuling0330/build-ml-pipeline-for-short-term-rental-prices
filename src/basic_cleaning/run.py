#!/usr/bin/env python
"""
Performs basic cleaning on the data and save the results in Weights & Biases parameters
"""
import argparse
import logging
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()
    logger.info("Download Artifact")
    artifact_path = run.use_artifact(args.input_artifact).file()
    
    logger.info("Removing Outliers")
    logger.info("Save cleaned dataset")



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="steps to clean the rawdata")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help="Name of the input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="Name of the output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="type of the artifact",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="description of the output",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=str,
        help="type of the artifact",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=str,
        help="type of the artifact",
        required=True
    )    
    args = parser.parse_args()

    go(args)
