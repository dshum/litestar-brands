import Status from "./status"

type Brand = {
  name: string
  hosts: string
  status: Status,
  db_name: string,
  created_at: string,
  settings: { [key: string]: string | number | object | never; },
}

export default Brand