import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule }   from '@angular/forms';
import { HttpModule }    from '@angular/http';

import { AppComponent } from './app.component';
import { SchoolsComponent } from './schools.component';
import { SchoolsService } from './schools.service';

@NgModule({
  declarations: [
    AppComponent,
    SchoolsComponent
  ],
  imports: [
    FormsModule,
    HttpModule,
    BrowserModule
  ],
  providers: [SchoolsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
