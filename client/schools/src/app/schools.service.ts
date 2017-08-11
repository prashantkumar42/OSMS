import { Injectable } from '@angular/core';
import { School } from './schools.component';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';


@Injectable()
export class SchoolsService {
    private schoolsUrl: string = "http://127.0.0.1:8000/services/getBatchNames";
    
    constructor(private http: Http) { }

    getSchools(): Promise<School[]> {
        return this.http.get(this.schoolsUrl)
             .toPromise()
             .then(response => response.json().response as School[])
             .catch(this.handleError);
    }

    private handleError(error: any): Promise<any> {
        console.error('An error occurred', error); // for demo purposes only
        return Promise.reject(error.message || error);
    }
}