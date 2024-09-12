import sys
import os
import zlib
import glob

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    # print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    
    command = sys.argv[1]

    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")

    elif command == "cat-file":
        param = sys.argv[2]
        blob_sha = sys.argv[3] 
        if param == "-p":
            content = open(f".git/objects/{blob_sha[:2]}/{blob_sha[2:]}", "rb").read()
            # content = open(f"./git/objects/{blob_sha}", "rb").read()
            d_content = zlib.decompress(content)
            str_content = d_content.decode("utf-8")
            str_content = str_content.split('\x00')
            str_content = str_content[1]
            print(str_content, end='')
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
