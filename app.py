blogs = dict()  # blog_name -> Blog Object


def menu():
    # Show the user the available Blogs
    # Let the user make a choice,
    # Do something with it,
    # then exit

    print_blogs()


def print_blogs():
    for key, blog in blogs.items():
        print("- {}".format(blog))