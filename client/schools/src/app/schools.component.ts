import { Component } from '@angular/core';
import {SchoolsService} from './schools.service';

export class School {
  id: Number;
  name: String;
}

let schoolsService: SchoolsService = new SchoolsService();

@Component({
  selector: 'schools',
  templateUrl: './schools.component.html',
  styleUrls: ['./schools.component.css']
})
export class SchoolsComponent {
  schools: School[] = schoolsService.getSchools();
}
