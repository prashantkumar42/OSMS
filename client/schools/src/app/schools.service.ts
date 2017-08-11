import { Injectable } from '@angular/core';
import { School } from './schools.component';
import { Headers, Http } from '@angular/http';
 
import { Observable }     from 'rxjs/Observable';
import 'rxjs/add/operator/map';


@Injectable()
export class SchoolsService {
    private schoolsUrl: string = "http://127.0.0.1:8000/services/getBatchNames";
    
    constructor(private http: Http) { }

    getSchools(): Observable<School[]> {
        return this.http.get(this.schoolsUrl)
             .map(response => response.json().response as School[])
    }

    private handleError(error: any): Promise<any> {
        console.error('An error occurred', error); // for demo purposes only
        return Promise.reject(error.message || error);
    }
}