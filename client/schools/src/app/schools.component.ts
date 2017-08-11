import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
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
  schools:School[];
  private schoolsService: SchoolsService;
  // methods
  constructor(schoolsServiceParam: SchoolsService) { 
    this.schoolsService = schoolsServiceParam;
  }
  getSchools(): void {
    this.schoolsService.getSchools().then(schools => this.schools = schools);
  }
  ngOnInit(): void {
    this.getSchools();
  }
}
