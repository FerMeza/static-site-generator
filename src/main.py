from block_markdown import markdown_to_blocks

def main():
    print(len(markdown_to_blocks("""
This is **bolded** paragraph              

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

                                                          
- This is a list

                                                   
- with items
""")))

if __name__ == "__main__":
    main()