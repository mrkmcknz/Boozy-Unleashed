# Boozy Unleashed
Code repository for the Bitcoin Unleashed presentation on `Build and List an NFT on Bitcoin`.

This code is not 'clean', lacks testing and is only really usable for the most basic of NFT collections. Additionally it does not make use of `threading` or `multiprocessing` to speed up the process.

## Requirements
* Python 3.10.3
* Poetry

## Installation
    poetry install

## Running
Boozies are created using the script located at `scripts/unleash.py`.

    poetry run python -m scripts.unleash

Once you have created boozies and uploaded these to IPFS you can update the CID using a script located at `scripts/update_cid.py`.

    poetry run python -m scripts.update_metadata
