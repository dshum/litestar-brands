import {Status} from "./status"

export type Brand = {
  name: string
  hosts: string
  status: Status
  db_name: string
  created_at: string
  settings: { [key: string]: string | number | object | never; }
}