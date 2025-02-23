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
                    print(type(response.registers[0]))
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

    @staticmethod
    def set_modbus_param_sql(client: ModbusSerialClient, db_connection: sqlite3.Connection,
                             param, value, unit_id=1):
        try:
            if client is None or not client.connected:
                return 'Отсутствует соединение с клиентом.'
            row = ModbusInteraction.get_param_address_from_sql(db_connection, param)
            if row is None:
                return 'Неизвестный параметр.'
            if isinstance(row[0], int) and isinstance(unit_id, int) and isinstance(value, int):
                response = client.write_register(address=row[0], value=value, slave=unit_id)
                if response.isError():
                    return f'Ошибка: {response}.'
                else:
                    return True
            else:
                return 'Передаваемые значения должны быть целыми числами.'
        except Exception as e:
            return f'Ошибка: {e}.'

    @staticmethod
    def get_modbus_param_sql(client: ModbusSerialClient, db_connection: sqlite3.Connection,
                             param=None, unit_id=1, for_set=False) -> tuple | str | int:
        try:
            if client is None or not client.connected:
                return 'Отсутствует соединение с клиентом.'

            row = ModbusInteraction.get_param_address_from_sql(db_connection, param)

            if row is None:
                return 'Неизвестный параметр.'
            response = client.read_holding_registers(address=row[0], slave=unit_id, count=1)
            if response.isError():
                return f'Ошибка: {response}.'
            elif for_set:
                return int(response.registers[0])
            else:
                return f'Прочитанное значение: {response.registers[0]}'
        except Exception as e:
            return f'Ошибка: {e}.'

    @staticmethod
    def get_param_address_from_sql(db_connection: sqlite3.Connection,
                                   param) -> int | None | Exception:
        if isinstance(db_connection, Exception):
            raise Exception(f'Ошибка: {db_connection}.')

        cursor = db_connection.cursor()
        db_param = cursor.execute("SELECT address FROM params WHERE param_name = ? LIMIT 1",
                                  (param,))
        row = db_param.fetchone()
        cursor.close()
        return row
