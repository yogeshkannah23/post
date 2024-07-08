import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

path = r"c:\Users\kanni\OneDrive\Desktop\posts\post_app\post"

MEDIA_ROOT = os.path.join(BASE_DIR,'static','media')
print(MEDIA_ROOT)