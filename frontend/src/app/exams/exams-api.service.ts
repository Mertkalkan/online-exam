import { HttpClient, HttpErrorResponse, HttpHeaderResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError, } from 'rxjs';
import { API_URL } from '../env';
import { Exam } from './exam.model';
import {catchError} from "rxjs/internal/operators";

@Injectable({
  providedIn: 'root'
})
export class ExamsApiService {

  constructor(private http: HttpClient) { }

  private _handleError(err: HttpErrorResponse) {
    return throwError(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getExams(): Observable<Exam[]> {
    return this.http
      .get<Exam[]>(`${API_URL}/exams`)
      .pipe(catchError(this._handleError));
      
  }

}
