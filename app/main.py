import sys
import os
import zlib

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    
    command = sys.argv[1]
    print(command)
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")

    if command == "cat-file":
        param = sys.argv[2]
        blob_sha = sys.argv[3] 
        if param == "-p":
            blob_dir = blob_sha[:2]
            print(blob_sha[2:])
            content = open(f"./git/{blob_sha[:2]}/{blob_sha[2:]}", "rb").read()
            d_content = zlib.decompress(content)
            print(d_content)

            return d_content
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
