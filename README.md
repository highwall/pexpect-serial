Introduction
------------

This is like pexpect, but it will work with serial port that you
pass it. You are reponsible for opening and close the serial port.
This allows you to use Pexpect with Serial port which pyserial supports.

Usage
-----

```python
    import serial
    from pexpect_serial import SerialSpawn

    with serial.Serial('COM1', 115200, timeout=0) as ser:
        ss = SerialSpawn(ser)
        ss.sendline('start')
        ss.expect('done')
```

License
-------
MIT
