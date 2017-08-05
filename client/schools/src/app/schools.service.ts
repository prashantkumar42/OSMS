import { Injectable } from '@angular/core';
import { School } from './schools.component';

let schools: School[] = [
    {id:1, name:"DPS"},
    {id:2, name:"KV"},
    {id:3, name:"JNV"}
]

@Injectable()
export class SchoolsService {
    getSchools(): School[] {
        return schools;
    }
}