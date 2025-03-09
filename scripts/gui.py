import tkinter as tk


class GUI:
    def __init__(self) -> None:
        self.instr: str = ""
        self.outstr: str = ""

        self.root = tk.Tk(
            screenName=None,
            baseName=None,
            className="tk",
            useTk=True,
            sync=False,
            use=None,
        )

        self.get_window()
        self.get_frame_input()
        self.get_frame_output()

        self.root.mainloop()

    # gui settings

    def get_window(self) -> None:
        self.root.geometry("600x900")
        self.root.title("Futhorcify")
        self.root.config(background="#212126")

    def get_frame_input(self) -> None:
        """
        get label
        get text field
        get button

        pack onto frame
        """
        self.input_frame = tk.Frame(
            self.root,
            width=500,
            height=100,
            borderwidth=10,
            relief=tk.GROOVE,
        )

        self.get_input_button()
        self.get_input_field()
        self.get_input_label()

        self.input_frame.pack(side="top")

    def get_input_field(self) -> None:
        # TODO
        self.input_field = tk.Text(
            self.root,
            borderwidth=10,
            relief=tk.GROOVE,
        )
        self.input_field.pack(side="bottom", fill="both")

    def get_input_label(self) -> None:
        # TODO
        self.input_label = tk.Label(
            # label for control
            self.input_frame,
            text="Select input data type",
        )
        self.input_label.pack(side="top")

    def get_input_button(self) -> None:
        # TODO
        self.input_button = tk.Button(
            self.input_frame,
            text="",
        )
        self.input_button.pack(side="top")

    def get_frame_output(self) -> None:
        """
        get label
        get text field

        pack onto frame
        """
        self.output_frame = tk.Frame(
            self.root,
            borderwidth=10,
            relief=tk.GROOVE,
        )

        self.get_output_label()
        self.get_output_field()

        self.output_frame.pack(side="bottom")

    def get_output_label(self) -> None:
        # TODO
        self.output_label = tk.Label(
            # label for control
            self.output_frame,
            text="Select output data type",
        )
        self.output_label.pack(side="top")

    def get_output_field(self) -> None:
        # TODO
        self.output_field = tk.Message(
            self.output_frame,
            text=self.outstr,
        )
        self.output_field.pack(side="bottom", fill="both")

    # Input and output functions

    def output_user_text(self) -> str:
        return self.outstr

    def input_text(self, instr: str) -> None:
        self.instr = instr


gui = GUI()
