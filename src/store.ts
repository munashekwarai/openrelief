import {mkdir,readFile,rename,writeFile} from "node:fs/promises";import {dirname} from "node:path";import type{AuditEvent,Conflict,FormDefinition,RecordData}from"./domain.js";
export interface State{forms:FormDefinition[];records:RecordData[];conflicts:Conflict[];audit:AuditEvent[];processedMutations:string[]}
export interface Store{read():Promise<State>;write(state:State):Promise<void>}
export const emptyState=():State=>({forms:[],records:[],conflicts:[],audit:[],processedMutations:[]});
export class MemoryStore implements Store{constructor(public state:State=emptyState()){}async read(){return structuredClone(this.state)}async write(value:State){this.state=structuredClone(value)}}
export class FileStore implements Store{constructor(private path:string){}async read(){try{return JSON.parse(await readFile(this.path,"utf8")) as State}catch(error:any){if(error.code==="ENOENT")return emptyState();throw error}}async write(state:State){await mkdir(dirname(this.path),{recursive:true});const temporary=`${this.path}.${process.pid}.tmp`;await writeFile(temporary,JSON.stringify(state,null,2),{mode:0o600});await rename(temporary,this.path)}}
