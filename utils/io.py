class Console():

    @staticmethod
    def header():
        print("")
        print("                         Elektro")
        print("   _____                .__  .__               .__        ")
        print("  /  _  \ ______   ____ |  | |  | _____ _______|__| ______")
        print(" /  /_\  \\____ \ /  _ \|  | |  | \__  \\_  __ \  |/  ___/")
        print("/    |    \  |_> >  <_> )  |_|  |__/ __ \|  | \/  |\___ \ ")
        print("\____|__  /   __/ \____/|____/____(____  /__|  |__/____  >")
        print("        \/|__|                         \/              \/ ")
        print("        Trainer for Apollaris Deep Learning Model")
        print("             Developed by Nicolas Fernandes")
        print("")


    def user_parameters(self):
        self.header()
        print("Select the mode:")
        print("(1) Generate combinations for multiple random systems")
        print("(2) Evaluate a specific system configuration for research")
        mode = input("Mode: ")