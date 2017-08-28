from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,  QSplitter

from stytra import LightsheetExperiment

from stytra.stimulation.protocols import MultistimulusExp06Protocol

from stytra.triggering import PyboardConnection

import multiprocessing


class GcMultistimExperiment(LightsheetExperiment):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        multiprocessing.set_start_method('spawn')
        self.pyb = PyboardConnection(com_port='COM3')

        protocol = MultistimulusExp06Protocol(repetitions=2, spontaneous_duration_pre=0, spontaneous_duration_post=0,
                         shock_args=dict(burst_freq=1, pulse_amp=3., pulse_n=1,
                 pulse_dur_ms=5, pyboard=self.pyb),
                                grating_args=dict(grating_period=10), calibrator=self.calibrator)

        self.set_protocol(protocol)
        self.dc.add_data_source('imaging', 'lightsheet_config', protocol, 'lightsheet_config')

        print('The protocol will take {} seconds or {}:{}'.format(protocol.duration,
                                                                  int(protocol.duration)//60,
                                                                  protocol.duration - 60*int(protocol.duration)//60))

        self.finished = False

        # Create window and layout:
        self.main_layout = QSplitter(Qt.Horizontal)
        self.main_layout.addWidget(self.widget_control)
        self.setCentralWidget(self.main_layout)

        # Show windows:
        self.show()
        self.show_stimulus_screen(True)

if __name__ == '__main__':
    app = QApplication([])
    exp = GcMultistimExperiment(app=app,
                                directory=r"C:\Users\portugueslab\Documents\Lightsheet_exp_metadata",
                                name='lightsheet',
                                wait_for_lightsheet=True)

    app.exec_()

