# Date: 2026.06.10
# Author: Aleksandr Vakulenko
# 
# This code was generated using DeepSeek and is an 
# automated translation of the corresponding 
# MATLAB R2021b code into Python.
# 
# Licensed after GNU GPL v3
# 

import serial
import time
from typing import Tuple, Optional

class HallBox:
    """
    Python translation of MATLAB Hall_box class.

    Replaces the aDevice base class and Connector_COM_RS232 with a
    standard pyserial Serial object. Retains original error parsing
    logic and command‑response protocol.
    """

    def __init__(self, com_port_num: int):
        """
        Parameters
        ----------
        com_port_num : int
            Non‑negative integer specifying the COM port number.
            E.g., 3 creates a connection to 'COM3'.
        """
        if not isinstance(com_port_num, int) or com_port_num < 0:
            raise ValueError("COM port number must be a non‑negative integer")
        self.port = f"COM{com_port_num}"
        # timeout chosen to allow the device time to answer;
        # adjust if your hardware requires a different value.
        self.ser = serial.Serial(port=self.port, baudrate=9600, timeout=1.0)

    # ------------------------------------------------------------------
    # Public methods (matching the original MATLAB interface)
    # ------------------------------------------------------------------
    def set_relay(self, cmd: str) -> Tuple[bool, Optional[int], Optional[str]]:
        """
        Send an arbitrary command and parse the response for errors.

        Parameters
        ----------
        cmd : str
            The command string (case insensitive).

        Returns
        -------
        err_status : bool
            True if the response indicates an error, False otherwise.
        err_no : int or None
            Error code extracted from the response (if any).
        err_comment : str or None
            Human‑readable description of the error (if any).
        """
        cmd_bytes = cmd.upper().encode('ascii') + b'\r'
        response = self._query(cmd_bytes)
        return self._error_parser(response)

    def idn(self) -> Tuple[str, bool, Optional[int], Optional[str]]:
        """
        Send the ``*IDN?`` identification command.

        Returns
        -------
        response : str
            Raw response string (error parsing is applied separately).
        err_status : bool
        err_no : int or None
        err_comment : str or None
        """
        cmd_bytes = b'*IDN?\r'
        response = self._query(cmd_bytes)
        err_status, err_no, err_comment = self._error_parser(response)
        return response, err_status, err_no, err_comment

    def rst(self) -> Tuple[bool, Optional[int], Optional[str]]:
        """
        Send the ``*RST`` reset command.

        Returns
        -------
        err_status : bool
        err_no : int or None
        err_comment : str or None
        """
        cmd_bytes = b'*RST\r'
        response = self._query(cmd_bytes)  # fix from original (response was undefined)
        return self._error_parser(response)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------
    def _query(self, cmd_bytes: bytes) -> str:
        """Write command, wait, read all available response bytes."""
        self.ser.write(cmd_bytes)
        time.sleep(0.1)                     # give device time to process
        if self.ser.in_waiting:
            response = self.ser.read(self.ser.in_waiting).decode('ascii', errors='ignore')
        else:
            response = ''
        # Strip any trailing whitespace / line terminators (the original
        # code used con_utils.discard_termination for the same purpose).
        return response.strip()

    @staticmethod
    def _error_parser(response: str) -> Tuple[bool, Optional[int], Optional[str]]:
        """
        Parse a response that may start with ``"RX ERROR: "``.

        Returns
        -------
        err_status, err_no, err_comment
            err_status is True if an error was found.
            err_no and err_comment are None when err_status is False.
        """
        err_no_list = [101, 102, 103, 200, 301, 302]
        err_comments_list = [
            'star cmd of size 4 is not an "*RST"',
            'star cmd of size 5 is not an "*IDN?"',
            "star cmd wrong size",
            "unknown cmd",
            "invalid symbol in cmd",
            "A symbol other than 'X' appeared twice."
        ]
        prefix = "RX ERROR: "
        n = len(prefix)

        if len(response) > n and response[:n] == prefix:
            err_status = True
            # Extract the error number that follows the prefix
            err_str = response[n:].strip()
            try:
                err_no = int(err_str)
            except ValueError:
                err_no = None

            if err_no in err_no_list:
                idx = err_no_list.index(err_no)
                err_comment = err_comments_list[idx]
            else:
                err_comment = "unknown error"
        else:
            err_status = False
            err_no = None
            err_comment = None

        return err_status, err_no, err_comment

    # ------------------------------------------------------------------
    # Cleanup
    # ------------------------------------------------------------------
    def close(self):
        """Explicitly close the serial port."""
        if self.ser.is_open:
            self.ser.close()

    def __del__(self):
        """Destructor – ensure the port is closed."""
        try:
            self.close()
        except Exception:
            pass