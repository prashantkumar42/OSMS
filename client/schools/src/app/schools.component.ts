import { Component, OnInit } from '@angular/core';

import { Observable }        from 'rxjs/Observable';
 


import {SchoolsService} from './schools.service';

export class School {
  id: Number;
  name: String;
}


@Component({
  selector: 'schools',
  templateUrl: './schools.component.html',
  styleUrls: ['./schools.component.css'],
  providers: [SchoolsService]
})
export class SchoolsComponent implements OnInit{
  // properties
  schools: Observable<School[]>;
  private schoolsService: SchoolsService;
  // methods
  constructor(schoolsServiceParam: SchoolsService) {
    this.schoolsService = schoolsServiceParam;
   }
  getSchools(): void {
    this.schools = this.schoolsService.getSchools();
  }
  ngOnInit(): void {
    this.getSchools();
  }
}
