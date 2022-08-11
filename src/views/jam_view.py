import time

import src.views.view_tools as vt
import src.wifi.wifi_availables_nw as nw
import src.views.detect_potential_targets as tgt
import src.views.home_view as h
import src.radio.jammer as j


class JamView:

    menus : list
    jammer : j.Jammer

    def __init__(self) -> None:

        # Menus choices initialization
        self.menus = [
              "433 MHz (ex: car remote controller)"
            , "1.57542 GHz (ex: L1 GPS band)"
            , "2.412 GHz (ex: Wifi channel 1)"
            , "2.437 GHz (ex: Wifi channel 6)"
            , "2.437 GHz (ex: Wifi channel 11)"
            , "Enter the frequency manually"
            , "Return to the home screen "
            , "Quit"]

        # Jammer initilization
        self.jammer = j.Jammer()

    def display(self):
        vt.new_page()

        print("Select a frequency to jam :\n")

        # menu selection
        choice = vt.choose_menu(self.menus)

        if (choice=='1'): # 433 Mhz
            # detect all availables targets
            nw.detect_nw()
            time.sleep(3)
            vt.new_page()

            # detect targets : networks hosted by drones
            tgt.main()
        
        elif (choice == '4'): # 2.437 GHz (ex: Wifi channel 6)
            self.jammer.set_center_freq(2437e6)
            self.jammer.start_jamming()

        elif (choice=='6'): # Enter manually
            freq = int(input("\nEnter the frequency to jam in MHz: "))

            time.sleep(3)
            vt.new_page()

            # perform jamming
            #tgt.main()

        elif (choice == '7'): # Home Screen
            view = h.HomeView()
            view.display()
    
def main():
    jam_view = JamView()
    JamView.display()


if __name__ == "__main__":
    main()