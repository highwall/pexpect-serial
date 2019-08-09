"""This is like pexpect, but it will work with serial port that you
pass it. You are reponsible for opening and close the serial port.
This allows you to use Pexpect with Serial port which pyserial supports.

PEXPECT LICENSE

    This license is approved by the OSI and FSF as GPL-compatible.
        http://opensource.org/licenses/isc-license.txt

    Copyright (c) 2012, Noah Spurrier <noah@noah.org>
    PERMISSION TO USE, COPY, MODIFY, AND/OR DISTRIBUTE THIS SOFTWARE FOR ANY
    PURPOSE WITH OR WITHOUT FEE IS HEREBY GRANTED, PROVIDED THAT THE ABOVE
    COPYRIGHT NOTICE AND THIS PERMISSION NOTICE APPEAR IN ALL COPIES.
    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""

from pexpect import spawn
from pexpect.exceptions import ExceptionPexpect

__all__ = ['SerialSpawn']


class SerialSpawn(spawn):
    """Extends pexpect.spawn to support serial connections created with
    pyserial."""

    def __init__(self, ser, args=None, **kwargs):
        """This takes a serial of pyserial as input. Please make sure the serial is open
        before creating SerialSpawn."""

        if not ser.isOpen():
            raise ExceptionPexpect('serial port is not ready')

        super().__init__(None, **kwargs)
        self.ser = ser
        self.name = '<serial port %s>' % ser.port
        self.child_fd = ser.fileno()
        self.closed = False

    def close(self):
        """Close the serial port.

        Calling this method a second time does nothing.
        """
        if not self.ser.isOpen():
            return

        self.flush()
        self.ser.close()
        self.closed = True

    def isalive(self):
        """This checks if the serial port is still valid."""
        return self.ser.isOpen()

    def send(self, s):
        "Write to serial, return number of bytes written"
        s = self._coerce_send_string(s)
        self._log(s, 'send')

        b = self._encoder.encode(s, final=False)
        return self.ser.write(b)
