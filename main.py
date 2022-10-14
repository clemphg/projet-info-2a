from vues.accueil_vue import VueAccueil

# This script is the entry point of your application

if __name__ == '__main__':
    # run the StartView
    current_view = VueAccueil()

    # while current_view is not none, the application is still running
    while current_view:
        # a border between view
        print("***********************************************************")
        # Display the info of the view
        current_view.display_info()
        # ask user for a choice
        current_view = current_view.make_choice()

    print("A bientôt !")
