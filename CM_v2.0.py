import random as rd
import tkinter as tk


class StandardMethod:
    object_name = ""
    object_desc = ""
    def check_desc(self):
        return ("Inspecting the "+self.object_name+"...\n it is: "+ self.object_desc)
    
class Mage(StandardMethod):
    def __init__(self):
        self.object_name = "mage"
        self.health_points = 100
        self.object_desc = "the playable character, on his way back deeper into the crypt"
        self.inventory = []
    def method_status(self):
        if 'staff' in self.inventory:
            inventory_phrase = "Equiped with his {}".format(self.inventory)
        else:
            inventory_phrase = "He wants his staff back\n and revenge on the ghost\n that stole his book of spells."
        if self.health_points == 100:
            health_phrase = "in top shape,"
        elif self.health_points >= 50:
            health_phrase = "wounded with {}HP left,".format(self.health_points)           
        elif self.health_points >= 1:
            health_phrase = "badly Wounded with {}HP left,".format(self.health_points)
        else: 
            health_phrase = "too hurt to continue..."
        return (self.check_desc() + "\nThe mage seems " + health_phrase + " and " + inventory_phrase)
    
class Crypt(StandardMethod):
    def __init__(self):
        self.object_name = "crypt"
        self.object_desc = "an ancient underground crypt, \n haunted by a well known ghost." 
        self.inventory = ['staff']
    def method_status(self):
        if 'staff' in self.inventory:
            inspect_phrase = "his {}".format(self.inventory)
        else:
            inspect_phrase = "that there is nothing here to pickup here anymore"
        return (self.check_desc() + " \n The mage notices " + inspect_phrase)
    
class Ghost(StandardMethod):
    def __init__(self):
        self.object_name = "ghost"
        self.health_points = 100
        self.object_desc = "an ancient apparition that\n the mage remembers fighting,\n in a long and gruesome battle."
    def method_status(self):
        if self.health_points == 100:
            health_phrase = "in top shape,"
        elif self.health_points >= 50:
            health_phrase = "wounded with {}HP left,".format(self.health_points)           
        elif self.health_points >= 1:
            health_phrase = "badly Wounded with {}HP left".format(self.health_points)
        else:
            health_phrase = "The ghost has vanished allready"
        return (self.check_desc() + "\nThe ghost seems " + health_phrase)
    
class Tk_layout(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cryptic Mage v2.0")        
        self.mage, self.crypt, self.ghost = Mage(), Crypt(), Ghost()
        self.action_any = 'Selected Action'
        self.action_var = tk.StringVar()
        self.action_var.set(self.action_any)
        self.action_label = tk.Label(self, textvariable=self.action_var)
        self.action_label.grid(column=7, row=1)
        self.target_any = 'Selected Target'
        self.target_var = tk.StringVar()
        self.target_var.set(self.target_any)
        self.target_label = tk.Label(self, textvariable=self.target_var)
        self.target_label.grid(column=7, row=2)
        self.message_log = '(\_/)\n(o.0)\n(___)\nRufmemory code training'
        self.message_var = tk.StringVar()
        self.message_var.set(self.message_log)
        self.message_label = tk.Label(self, textvariable=self.message_var)
        self.message_label.grid(column=1, row=3)
        self.guide_label = tk.Label(self, text="Click on desired action,\n then select a target\n and presss enter or go")
        self.guide_label.grid(column=1, row=1)
        self.log_label = tk.Label(self, text='Message log:')
        self.log_label.grid(column=1, row=2)
        self.target_label = tk.Label(self, text='Target:')
        self.target_label.grid(column=2, row=2)
        self.action_label = tk.Label(self, text='Action:')
        self.action_label.grid(column=2, row=1)
        go_btn = tk.Button(self, text='Go', command=self.exec_act_tgt)
        go_btn.grid(column=7, row=3)
        inspect_btn = tk.Button(self, text='Inspect', command=self.select_inspect)
        inspect_btn.grid(column=3, row=1)
        mage_btn = tk.Button(self, text='Mage', command=self.select_mage)
        mage_btn.grid(column=3, row=2)
        for child in self.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        self.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        self.bind('<Return>', self.exec_act_tgt)
        
    def select_inspect(self):
        self.action_var.set('Inspect')
    def select_pickup(self):
        self.action_var.set('Pickup')
    def select_cast(self):
        self.action_var.set('Cast')
    def select_mage(self):
        self.target_var.set('Mage')
    def select_crypt(self):
        self.target_var.set('Crypt')
    def select_staff(self):
        self.target_var.set('Staff')
    def select_ghost(self):
        self.target_var.set('Ghost')
    def select_guess(self):
        self.action_var.set('Guess')
    def select_blue(self):
        self.target_var.set('Blue charm')
    def select_red(self):
        self.target_var.set('Red charm')
        
    def exec_act_tgt(self, *args):
        current_tgt = self.target_var.get()
        current_act = self.action_var.get()
        if current_tgt == 'Mage' and current_act == 'Inspect':
            self.message_var.set(self.mage.method_status())
            crypt_btn = tk.Button(self, text='Crypt', command=self.select_crypt)
            crypt_btn.grid(column=4, row=2)
        elif current_tgt == 'Crypt' and current_act == 'Inspect':
            self.message_var.set(self.crypt.method_status())
            staff_btn = tk.Button(self, text='Staff', command=self.select_staff)
            staff_btn.grid(column=5, row=2)
            pickup_btn = tk.Button(self, text='Pickup', command=self.select_pickup)
            pickup_btn.grid(column=4, row=1)
        elif current_tgt == 'Staff' and current_act == 'Inspect':
            self.message_var.set('The lost staff of this mage,\n picking it up might be a good idea')
        elif current_tgt == 'Staff' and current_act == 'Pickup':
            staff = self.crypt.inventory.pop()
            self.mage.inventory.append(staff)
            self.message_var.set("The mage can now fight the ghost again.\n Try to cast your spells at the ghost!")
            ghost_btn = tk.Button(self, text='Ghost', command=self.select_ghost)
            ghost_btn.grid(column=6, row=2)
            cast_btn = tk.Button(self, text='Cast', command=self.select_cast)
            cast_btn.grid(column=5, row=1)
        elif current_tgt == 'Ghost' and current_act == 'Inspect':
            self.message_var.set(self.ghost.method_status())
        elif current_tgt == 'Ghost' and current_act == 'Cast':
            self.mage_attacking = rd.randint(4,33)
            self.ghost_attacking = rd.randint(1,25)
            self.message_var.set("The mage throws a fireball\n removing {}HP\nThe ghost retaliates and emmits a\n lightning strike removing {}HP".format(self.mage_attacking, self.ghost_attacking))
            self.ghost.health_points = self.ghost.health_points - self.mage_attacking
            self.mage.health_points = self.mage.health_points - self.ghost_attacking
            if self.mage.health_points <= 0:
                self.message_var.set("The mage is too wounded and\n has to warp out of here again.\n(\_/)\n(~.~)\n(___)")
            elif self.ghost.health_points <= 0:
                self.magic_choice = rd.choice(['Red charm','Blue charm'])
                self.message_var.set("The ghost vanishes as a dusty cloud, leaving a\n familiar book, yet something is still odd.\n The mage gasps, as he notices a strange seal,\n He now has to guess right charm colour that will\n unlock the seal. Make the final guess!")
                guess_btn = tk.Button(self, text='Guess', command=self.select_guess)
                guess_btn.grid(column=6, row=1)
                blue_btn = tk.Button(self, text='Red charm', command=self.select_red)
                blue_btn.grid(column=5, row=3)
                red_btn = tk.Button(self, text='Blue charm', command=self.select_blue)                    
                red_btn.grid(column=6, row=3)
        elif current_act == 'Guess' and current_tgt == 'Red charm' or current_tgt == 'Blue charm':
            if current_tgt == self.magic_choice:
                self.message_var.set("The mage now relieved\n continues on his journey\n(\_/)\n(^_^)\n(___)")
            else:
                self.message_var.set("The mage is now trapped in another dimension! \n(\_/)\n(-_-)\n(___)")
        else:
            self.message_var.set("This action is not possible\n(\_/)\n(O.O)\n(___)")
                 
tk_run = Tk_layout()
tk_run.mainloop()    
