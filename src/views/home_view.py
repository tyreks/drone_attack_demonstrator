import time

import src.views.view_tools as vt
import src.wifi.wifi_availables_nw as nw
import src.views.detect_potential_targets as tgt
import src.views.home_view as h
import src.views.jam_view as j


class HomeView:

    menus : list

    def __init__(self) -> None:
        self.menus = [
              "Detect"
            , "Hijack"
            , "Spoof GPS"
            , "Jam"
            , "Settings"
            , "Quit"]

    def display(self):
        vt.new_page()
        # menu selection
        choice = vt.choose_menu(self.menus)

        if (choice=='1'): # "detect targets" choice
            # detect all availables targets
            nw.detect_nw()
            time.sleep(3)
            vt.new_page()

            # detect targets : networks hosted by drones
            tgt.main()
        
        elif (choice == '4'):
            view = j.JamView()
            view.display()
    

    
def main():
    home_page = HomeView()
    home_page.display()


if __name__ == "__main__":
    main()