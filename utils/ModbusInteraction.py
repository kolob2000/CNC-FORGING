import sqlite3
from http.client import responses

from pymodbus.client import ModbusSerialClient


class ModbusInteraction:
    @staticmethod
    def write_modbus_register(client: ModbusSerialClient, register: int, value: int, unit_id=1):
        try:
            if client is None or not client.connected:
                return 'Отсутствует соединение с клиентом.'
            if isinstance(register, int) and isinstance(unit_id, int) and isinstance(value, int):
                response = client.write_register(address=register, value=value, slave=unit_id)
                if response.isError():
                    return f'Ошибка: {response}.'
                else:
                    return f"Записано значение: {value} в регистр {register}."
            else:
                return 'Передаваемые значения должны быть целыми числами.'
        except Exception as e:
            return f'Ошибка: {e}.'

    @staticmethod
    def read_modbus_register(client: ModbusSerialClient, register: int, unit_id=1):
        try:
            if client is None or not client.connected:
                return 'Отсутствует соединение с клиентом.'
            if isinstance(register, int) and isinstance(unit_id, int):
                response = client.read_holding_registers(address=register, slave=unit_id, count=1)
                if response.isError():
                    return f'Ошибка: {response}.'
                else:
                    return f'Прочитанное значение: {response.registers[0]}'
            else:
                return 'Передаваемые значения должны быть целыми числами.'
        except Exception as e:
            return f'Ошибка: {e}.'

    @staticmethod
    def write_modbus_command_sql(client: ModbusSerialClient, db_connection: sqlite3.Connection, command: str,
                                 unit_id=1):
        try:
            if client is None or not client.connected:
                return 'Отсутствует соединение с клиентом.'
            elif isinstance(db_connection, Exception):
                return f'Ошибка: {db_connection}.'
            cursor = db_connection.cursor()
            command = cursor.execute("SELECT address, value FROM controls WHERE command_name = ? LIMIT 1",
                                     (command,))
            row = command.fetchone()
            cursor.close()
            if row is None:
                return 'Неизвестная команда.'
            response = client.write_register(address=int(row[0]), value=int(row[1]), slave=unit_id)
            if response.isError():
                return f'Ошибка: {response}.'
            else:
                return f"Команда: {command} выполнена."
        except Exception as e:
            return f'Ошибка: {e}.'
