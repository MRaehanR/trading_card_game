def print_warning(text):
    print(text_colors["warning"]+text+text_colors["end_color"])
    
def print_error(text):
    print(text_colors["error"]+text+text_colors["end_color"])
    
def print_success(text):
    print(text_colors["success"]+text+text_colors["end_color"])
    
text_colors = {
    "warning": "\033[93m",
    "error": "\033[91m",
    "success": "\033[92m",
    "end_color": "\033[0m"
}