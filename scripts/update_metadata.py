import json
import os


def main():
    old_cid = "CHANGEME"
    new_cid = "QmcM3YpV9ZSpLS477rMLdNf2xzNCyMfLcc82XnaxA7dtZ4"
    metadata = "output/metadata"
    for metadata_file in os.listdir(metadata):
        with open(f"{metadata}/{metadata_file}") as infile:
            data = json.load(infile)
        data["image"] = data["image"].replace(old_cid, new_cid)
        with open(f"{metadata}/{metadata_file}", "w") as outfile:
            json.dump(data, outfile)


if __name__ == "__main__":
    main()
