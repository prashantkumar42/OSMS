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
    this.schools = this.schoolsService.getSchools();
  }
  ngOnInit(): void {
    this.getSchools();
  }
}
