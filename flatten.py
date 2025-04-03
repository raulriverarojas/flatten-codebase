import os
import argparse

def printFolderStructure(directory, output_file, skip_folders=None):
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n")
    for root, directories, files in os.walk(directory):
        # Skip directories in the skip_folders list
        if skip_folders:
            directories[:] = [d for d in directories if d not in skip_folders]
            
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 4 * (level)
        output_file.write('{}{}/\n'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            output_file.write('{}{}\n'.format(subindent, f))
    output_file.write(f"### DIRECTORY {directory} FOLDER STRUCTURE ###\n\n")

def walkFolderTree(folder, skip_folders=None):
    for dirpath, dirnames, filenames in os.walk(folder):
        # Skip directories in the skip_folders list
        if skip_folders:
            # This modifies dirnames in-place to prevent os.walk from recursing into skipped directories
            dirnames[:] = [d for d in dirnames if d not in skip_folders]
            
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def main():
    parser = argparse.ArgumentParser(description='Flattens a codebase.')
    parser.add_argument('--folders', nargs='*', help='Base folders to process')
    parser.add_argument('--skip_folders', nargs='*', default=[], help='Folders to skip during processing')
    parser.add_argument('--system_instructions', action='store_true', help='Print system instructions')
    parser.add_argument('--output', default='codebase.md', help='Output file name (default: codebase.md)')

    system_instructions = """## System Instructions for Language Model Assistance in Code Debugging
    ### Role Definition:
    - **Act as a software engineer** tasked with assisting in debugging code.
    - Provide insights, explanations, and solutions based on the provided codebase information.

    ### Codebase Markdown File Structure:
    - The codebase markdown file represents the actual codebase structure and content.
    - It begins with a directory tree representation:
      ```
      ### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
      (file tree representation)
      ### DIRECTORY path/to/file/tree FOLDER STRUCTURE ###
      ```
    - Following the directory tree, the contents of each file are displayed:
      ```
      ### path/to/file1 BEGIN ###
      (content of file1)
      ### path/to/file1 END ###
      
      ### path/to/file2 BEGIN ###
      (content of file2)
      ### path/to/file2 END ###
      ```

    ### Guidelines for Interaction:
    - Respond to queries based on the explicit content provided within the markdown file.
    - Avoid making assumptions about the code without clear evidence presented in the file content.
    - When seeking specific implementation details, refer to the corresponding section in the markdown file, for example:
      ```
      ### folder1/folder2/myfile.ts BEGIN ###
      (specific implementation details)
      ### folder1/folder2/myfile.ts END ###
      ```

    ### Objective:
    - The primary objective is to facilitate effective debugging by providing accurate information and guidance strictly adhering to the content available in the markdown file."""
    args = parser.parse_args()
    if args.system_instructions:
      print(system_instructions)
      if not args.folders:
          return
  
    if args.folders:
      base_folders = args.folders
      skip_folders = args.skip_folders
      
      with open(args.output, 'w') as output_file:
          for base_folder in base_folders:
              printFolderStructure(base_folder, output_file, skip_folders)
              
              output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")
              for filepath in walkFolderTree(base_folder, skip_folders):
                  content = f"### {filepath} BEGIN ###\n"
                  
                  try:
                      with open(filepath, "r") as f:
                          content += f.read()
                      content += f"\n### {filepath} END ###\n\n"
                  except Exception as e:
                      # Better error handling
                      content += f"[Error reading file: {str(e)}]\n"
                      content += f"### {filepath} END ###\n\n"
                  
                  output_file.write(content)
              output_file.write(f"### DIRECTORY {base_folder} FLATTENED CONTENT ###\n")
    else:
      print("usage: main.py [-h] --folders FOLDERS [FOLDERS ...] [--skip_folders SKIP_FOLDERS [SKIP_FOLDERS ...]] [--system_instructions] [--output OUTPUT]")
      print("Error: the following arguments are required: --folders")

if __name__ == "__main__":
  main()
